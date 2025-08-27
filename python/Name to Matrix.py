from math import ceil
# https://www.codewars.com/kata/5a91e0793e9156ccb0003f6e/train/python

def matrixfy(st):  
    k = 0
    if st == '': return 'name must be at least one letter'
    sq_len = ceil(len(st) ** 0.5)
    print(sq_len)
    res_list = [["." for j in range(sq_len)] for i in range(sq_len)]

    for i in range(sq_len):
        for j in range(sq_len):
            try:
                res_list[i][j] = st[k]
                k += 1
            except:
                return res_list
    return res_list

# matrixfy("Beyonce"), [["B", "e", "y"], ["o", "n", "c"], ["e", ".", "."]]

print(matrixfy("G"))