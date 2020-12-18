import numpy as np
import pulp


def diff_time(num,bus_id):
    floor_ = int(num / bus_id)*bus_id
    if floor_ < num:
        floor_ += bus_id
    assert (floor_ - bus_id) >= 0
    return floor_ - num


def part2(input_path):
    """
    input: b_1,b_2,...,b_n
    Want temp_id s.t.
    diff_time(temp_id,b_1) = c0 (0)
    diff_time(temp_id,b_2) = c1
    diff_time(temp_id,b_3) = c2
    diff_time(temp_id,b_4) = c3
    ......
    diff_time(temp_id,b_n) = b_1

    Or better to go for LP?
    want min temp_id s.t
    min temp_id, s.t.

    (temp_id + c0) - x1*b_1 = 0
    (temp_id + c1) - x2*b_2 = 0
    (temp_id + c2) - x3*b_3 = 0
    ...
    temp_id + cn) - xn*bn   =  0
    xn*bn - b1(x1 + 1) = 0

    LP take 2

    minimize
    c1*b1

    subject to
    c2*b2 = c1*b1 + t2
    c3*b3 = c1*b1 + t3
    ....
    cn*bn = tn
    (c1 + 1)*b1 = cn*bn



    :return:
    """

    lines = open(input_path).readlines()
    b_id_raw = lines[1].split(",")
    b_ids = [b for b in b_id_raw if b != "x"]
    t_n = [b_id_raw.index(b_i) for b_i in b_ids]
    b_ids = [int(b_id) for b_id in b_ids]
    unknows = np.zeros(len(b_ids))

    def guess_timestamp(guess,b_ids,unknowns,t_n):


        eqs = []
        for i in range(len(b_ids)):
            eq = unknowns.copy()
            eq[i] = b_ids[i]
            eqs.append(eq)

        eq = unknowns.copy()
        eq[-1] = b_ids[-1]
        eq[1] = -1*b_ids[0]
        eqs.append(eq)
        #t_n *= -1
        t_n = t_n + [-1*b_ids[0]]

        a = np.array(eqs)
        b = np.array(t_n)

        guess_vect = np.ones(len(b_ids) + 1)*guess
        guess_vect[-1] = 0

        b = np.add(guess_vect,b)


        try:
            x = np.linalg.solve(a[:-1],b[:-1])
            return True
        except:
            return False

    guess = 1
    while(True):
        res = guess_timestamp(guess,b_ids,unknows,t_n)
        if res:
            print(f"answer is {guess}")
            break
        else:
            guess += 1

    print("Answer is")


def part2_lp(input_path):
    """

    :param input_path:
    :return:
    """

    lines = open(input_path).readlines()
    b_id_raw = lines[1].split(",")
    ## KNOWNS bus_id , time between each as constraint
    b_ids = [b for b in b_id_raw if b != "x"]
    t_n = [b_id_raw.index(b_i) for b_i in b_ids] # time t increments
    b_ids = [int(b_id) for b_id in b_ids] # buss ids

    ## Unknown Constant multipliers s.t b_id * mulitplier = min timestamp

    problem = pulp.LpProblem("Advent 13 part 2",pulp.LpMinimize)

    # create list of variables
    vars = []
    for b_id in b_ids:
        var_name = f"c_{b_id}"
        var_i = pulp.LpVariable(var_name,1,None,pulp.LpInteger)
        vars.append(var_i)

    # Problem to solve is minimum multiplier C1 s.t. constraints hold
    problem += vars[0]*b_ids[0]

    # Now add all constraints
    for var_id,b_id ,t_n in zip(vars[1:],b_ids[1:],t_n[1:]):
        problem += var_id*b_id == vars[0]*b_ids[0] + t_n

    problem.writeLP("prob13.lp")

    problem.solve()

    print("Status:", pulp.LpStatus[problem.status])

    for v in problem.variables():
        print(v.name, "=", v.varValue)

    obj= pulp.value(problem.objective)
    print("Muliplie is " + str(obj))





def run(input_path):

    lines = open(input_path).readlines()
    depart_time= int(lines[0])
    buss_sched = [int(id) for id in lines[1].split(",") if id != "x"]

    times = [diff_time(depart_time,bus_id) for bus_id in buss_sched]

    wait_time = min(times)
    bus_id = buss_sched[times.index(wait_time)]
    ans = bus_id*wait_time
    print(f"Answer = {ans}")


if __name__ == "__main__":

    input_path = "data/day13_test.txt"

    part2_lp(input_path)

