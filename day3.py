
def run(input_path,start=(0,0),slope=(3,1)):
    """
    :param input_path:
    :return:
    """
    lines = open(input_path).readlines()
    lines = [line.strip("\n") for line in lines]
    rows = len(lines)
    cols = len(lines[0])
    mx , my = slope
    poss_moves = int(rows / my)
    currx , curry = start
    num_trees = 0
    for _ in range(poss_moves):
        char = lines[curry][currx % cols]
        if char == "#":
            num_trees += 1

        currx += mx
        curry += my

    print(f"Number of trees hit {num_trees}")

    return num_trees


if __name__ == "__main__":
    input_path = "data/day3.txt"

    run_part_1 = 1
    if run_part_1:
        print("running part 1")
        run(input_path)

    run_part_2 = 1
    if run_part_2:
        print("running part 2")
        run1 = run(input_path,slope=(1,1))
        run2 = run(input_path,slope=(3,1))
        run3 = run(input_path,slope=(5,1))
        run4 = run(input_path,slope=(7,1))
        run5 = run(input_path,slope=(1,2))

        print(f"Product of trees = {run1*run2*run3*run4*run5}")

