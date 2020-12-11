import numpy as np

def convert_to_matrix(lines):
    n = len(lines)
    m = len(lines[0]) - 1
    occupied_mat = np.zeros((n,m))
    empty_mat = np.zeros((n,m))
    valid_mat = empty_mat.copy()

    for i in range(n):
        line_i = lines[i].replace("\n","")
        occ_index = [j for j, c in enumerate(line_i) if c == "#"]
        occupied_mat[i,occ_index] = 1
        empty_index = [j for j, c in enumerate(line_i) if c == "L"]
        empty_mat[i, empty_index] = 1
        valid_mat[i, empty_index + occ_index] = 1

    return occupied_mat,empty_mat,valid_mat

def update_kernel(occ_mat,empty_mat,valid_mat):

    n , m = occ_mat.shape
    convolv = np.ones((3,3))
    convolv[1][1] = 0

    padded_occ = np.zeros((n + 2, m + 2))
    padded_occ[1:-1,1:-1] = occ_mat
    empty_indeces = np.where(empty_mat == 1)
    occ_update_index = np.where(occ_mat == 1)

    new_occ_mat = occ_mat.copy()
    new_empty_mat = empty_mat.copy()

    if len(empty_indeces[0]) > 0:
        empty_indeces = zip(*empty_indeces)
        for i , j in empty_indeces:
            i = i + 1
            j = j + 1
            update_chunk = padded_occ[i - 1:i + 2,j - 1:j + 2]
            sum = np.multiply(update_chunk,convolv).sum()
            if sum == 0:
                new_occ_mat[i - 1][j - 1] = 1
                new_empty_mat[i - 1][j - 1] = 0

    if len(occ_update_index[0]) > 0:
        occ_update_index = zip(*occ_update_index)
        for i , j in occ_update_index:
            i = i + 1
            j = j + 1
            update_chunk = padded_occ[i - 1:i + 2,j - 1:j + 2]
            sum = np.multiply(update_chunk,convolv).sum()
            if sum >= 4:
                new_empty_mat[i - 1][j - 1] = 1
                new_occ_mat[i - 1][j - 1] = 0

    new_occ_mat = np.multiply(new_occ_mat,valid_mat)
    new_empty_mat = np.multiply(new_empty_mat,valid_mat)
    return new_occ_mat , new_empty_mat


def run(data_path):
    lines = open(data_path).readlines()

    occ_mat,empty_mat,valid_mat = convert_to_matrix(lines)

    while(True):
        new_occ_mat , new_empty_mat = update_kernel(occ_mat,empty_mat,valid_mat)

        diff1 = (np.abs(new_occ_mat - occ_mat)).sum()
        diff2 = (np.abs(new_empty_mat - empty_mat)).sum()
        occ_mat = new_occ_mat.copy()
        empty_mat = new_empty_mat.copy()
        if (diff1 + diff2 == 0):
            break

    num_occ = len(np.where(occ_mat == 1)[0])
    print(f"Number of occupied seats after converged = {num_occ}")


if __name__ == "__main__":

    data_path = "data/day11.txt"

    run(data_path)


