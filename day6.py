
def clean_line(line):
    line = line.strip()
    line = line.replace("\n","")
    return line

def run_2(data_input):

    total = 0
    with open(data_input, "r") as reader:

        questions = ""
        newline = True
        while True:
            line = reader.readline()
            if line == "\n":
                total += len(set(questions))
                questions = ""
                newline = True
            elif line == "":
                total += len(set(questions))
                break
            else:
                line = clean_line(line)
                if not newline:
                    for c in questions:
                        if c not in line:
                            questions = questions.replace(c,"")
                else:
                    questions = line
                    newline = False

    print(f"Total = {total}")


def run(data_input):

    total = 0
    with open(data_input, "r") as reader:

        questions = []
        while True:
            line = reader.readline()
            if line == "\n":
                total += len(set(questions))
                questions = []

            elif line == "":
                total += len(set(questions))
                break
            else:
                line = clean_line(line)
                chars = [c for c in line]
                questions += chars

    print(f"Total = {total}")

if __name__ == "__main__":

    data_input = "data/day6.txt"
    run_2(data_input)