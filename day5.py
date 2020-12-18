
def binary_code_search(code,size,L,U):
    range = [0, size - 1]
    for c in code:
        dist = int((range[1] - range[0]) / 2) + 1
        if c == L:
            range[1] -= dist
        elif c == U:
            range[0] += dist
        else:
            raise Exception(f"Unknown code {c}")
    assert range[0] == range[1]
    return range[0]


def clean_line(line):
    line = line.strip()
    line = line.replace("\n","")
    return line

def run(data_path):

    lines = open(data_path).readlines()
    max_seat_id = 0
    seat_id_list = []
    row_list = []
    for line in lines:
        line = clean_line(line)
        row = binary_code_search(line[:7],128,"F","B")
        seat = binary_code_search(line[7:],8,"L","R")
        seat_id = row*8 + seat
        seat_id_list.append(seat_id)
        row_list.append(row)
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    seat_id_list.sort()
    row_list.sort()
    #print(seat_id_list)
    last_seat = seat_id_list[0]
    for seat_id in seat_id_list[1:]:
        diff = seat_id - last_seat
        if diff > 1:
            print(f"Missing seat id {last_seat + 1}")
        last_seat = seat_id
    #print(set(row_list))
    print(f"Max seat id = {max_seat_id}")

if __name__ == "__main__":
    data_path = "data/day5.txt"
    run(data_path)