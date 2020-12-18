def run(data_path):

    lines = open(data_path).readlines()

    adapt_list = [int(num.replace("\n","")) for num in lines]

    adapt_list.sort()
    print(adapt_list)

    start_adaptar = 0
    diff_1_count = 0
    diff_3_count = 0
    lowest_val = adapt_list[0]

    for val in adapt_list:

        if val - start_adaptar == 1:
            diff_1_count += 1
            start_adaptar = val

        elif val - start_adaptar == 3:
            diff_3_count += 1
            start_adaptar = val
        else:
            print("oopsy")
            print(val)
            print(start_adaptar)

    print(f"Num diff 1 count {diff_1_count}")
    print(f"Num diff 3 count {diff_3_count}")
    print((diff_3_count + 1)*diff_1_count)


def count_perms(data_path):

    lines = open(data_path).readlines()

    adapt_list = [int(num.replace("\n","")) for num in lines]

    adapt_list.sort()

    def sub_route(i,adapt_list):
        num_i = adapt_list[i]
        num_range = 0
        n = len(adapt_list)
        for j in range(1,4):
            if i + j > n - 1:
                break
            if adapt_list[i + j] <= num_i + 3:
                num_range += 1
            else:
                break
        return num_range

    perms = 1

    curr_index = 0
    adapt_list = [0] + adapt_list
    print(adapt_list)
    perms_map = {1:1, 2:3, 3:4}
    while(True):
        print(f"Current index = {curr_index}")
        print(f"CUrrent num = {adapt_list[curr_index]}")
        nums = sub_route(curr_index,adapt_list)
        print(nums)
        if nums == 0:
            curr_index += 1
        else:
            perms *= perms_map[nums]
            curr_index += (nums)
        if curr_index >= len(adapt_list):
            break

    print(perms)



if __name__ == "__main__":
    data_path = "data/day10_test.txt"
    #count_perms(data_path)
    lines = open(data_path).readlines()

    adapt_list = [int(num.replace("\n","")) for num in lines]

    #adapt_list.sort()
    #print(adapt_list)
