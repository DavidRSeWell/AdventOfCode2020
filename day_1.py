import numpy as np

def main(data_path):
    lines = open(data_path).readlines()
    lines = [int(l) for l in lines]
    lines.sort()
    lines = np.array(lines)
    diff = 2020 - lines
    solutions = []
    for i in range(len(lines)):
        if diff[i] in lines:
            j = np.where(lines == diff[i])[0]

            solutions.append((i,j))
    for i,j in solutions:
        print("Winnder" +  "\n")
        print(f"{lines[i]} and {lines[j]}")
        print("Answer: " + str(lines[i]*lines[j]))

if __name__ == "__main__":
    data_path = "data/day_1_input.txt"
    main(data_path)
