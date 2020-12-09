import numpy as np

def main(data_path):
    lines = open(data_path).readlines()
    lines = [int(l) for l in lines]
    lines.sort()
    lines = np.array(lines)
    diffs = 2020 - lines
    solutions = []
    n_lines = len(lines)
    
    for i in range(n_lines):
        diff = diffs[i]
        diffs2 = diff - lines
        for j in range(n_lines):
            diff2 = diffs2[j]
            if diff2 in lines:
                k = np.where(lines == diff2)[0]
                solutions.append((i,j,k))
    
    for i,j,k in solutions:
        print("Winnder" +  "\n")
        print(f"{lines[i]} and {lines[j]} and {lines[k]}")
        print("Answer: " + str(lines[i]*lines[j]*lines[k])) 

if __name__ == "__main__":
    data_path =  "./day_1_input.txt"
    main(data_path)
