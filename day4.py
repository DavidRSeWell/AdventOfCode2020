
"""
Advent of Code Day 4 Puzzle
author: Ethan Lew
--- Day 4: Passport Processing ---
"""
import re
import typing as typ

def clean_string(x):
    x = x.strip()
    x = x.replace("\n",x)
    return x
def valid_height(x):
    x = x.replace("\n","")
    unit = x[-2:]
    val = x[:-2]
    try:
        assert unit in ["cm", "in"]
        assert int(val)
    except:
        return False
    val = int(val)
    if unit == "cm":
        if 150 <= val <= 193:
            return True
    elif unit == "in":
        if 59 <= val <= 96:
            return True
    return False

def valid_ecl(x):
    x = x.replace("\n","")
    req_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    try:
        assert len(x) == 3
        assert x in req_list
        return True
    except:
        return False

def check_key_values(key_values):

    val_check = {"byr": lambda x: (int(x) >= 1920 and int(x) <= 2002) and True or False,
                "iyr": lambda x: (int(x) >= 2010 and int(x) <= 2020) and True or False,
                "eyr": lambda x: (int(x) >= 2020 and int(x) <= 2030) and True or False,
                "hgt": lambda x: valid_height(x),
                "hcl": lambda x: re.match(r"(^#[0-9a-f]{6}\Z)",clean_string(x)),
                "ecl": lambda x: valid_ecl(x),
                "pid": lambda x: re.match(r"(^[0-9]{9}\Z)",clean_string(x))}

    if not check_keys(key_values):
        return False

    for kv in key_values:
        k,v = kv
        if k == "cid": continue
        if not val_check[k](v):
            return False

    return True

def check_keys(key_values):
    req_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

    num_valid_keys = 0
    for key,value in key_values:
        if key in req_keys:
            num_valid_keys += 1

    if num_valid_keys == 7:
        return True


def check_validity(key_values,part_two=False):
    if part_two:
        return check_key_values(key_values)
    else:
        return check_keys(key_values)


def run(data_path,part_two=False):

    """
    Required keys and constraints
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    num_valid = 0
    num_line = 0
    invalids = []
    with open(data_path, "r") as reader:
        # Read and print the entire file line by line

        key_values = []
        while True:  # The EOF char is an empty string
            line = reader.readline()

            if line == "\n" or line == "":
                if check_validity(key_values,part_two):
                    num_valid += 1
                else:
                    print(f"invalid line {num_line}")
                    invalids.append(num_line)
                num_line += 1
                key_values = []
                if line == "":
                    break
                continue

            line = line.split(" ")
            for kv in line:
                k = tuple(kv.split(":"))
                key_values.append(k)

    print(f"Num valid = {num_valid}")
    return invalids


if __name__ == "__main__":
    data_path = "data/day4.txt"
    check = ('hgt', '184cm\n')
    my_invalids = run(data_path,part_two=True)

