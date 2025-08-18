# https://www.codewars.com/kata/590938089ff3d186cb00004c/train/python

# b[0] = a[0] + a[1] + ... + a[n - 2] + a[n - 1]
# b[1] =        a[1] + ... + a[n - 2] + a[n - 1]
# ...
# b[n - 2] =                 a[n - 2] + a[n - 1]
# b[n - 1] =                            a[n - 1]

def suffix_sums(arr):
    arr_b = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            arr_b[i] += arr[j] 
    return arr_b



print(suffix_sums([1, 2, 3, -6]))