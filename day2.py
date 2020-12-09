


def rule1(min,max,letter,pwd):
    letter_count = pwd.count(letter)
    if (letter_count <= max) and (letter_count >= min):
        return True
    else:
        return False

def rule2(min,max,letter,pwd):

    check1 = (pwd[min - 1] == letter)
    check2 = (pwd[max - 1] == letter)
    if check1:
        if check2:
            return False
        else:
            return True

    else:
        if check2:
            return True

    return False

def run(file_path,rule=rule2):

    lines = open(file_path).readlines()
    valid = 0
    for line in lines:
        line = line.split()
        min , max = tuple(line[0].split('-'))
        min, max = int(min), int(max)
        letter = line[1].replace(':', '')

        if rule(min,max,letter,line[2]):
            valid += 1

    print(f"Num valid = {valid}")


if __name__ == '__main__':
    path = './day2.txt'

    print("Running part 1")
    run(path,rule1)
    print("Running part 2")
    run(path, rule2)


