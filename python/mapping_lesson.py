def mult_on_2(ls):
    return ls * 2

testlist = [1, 5, 66]
# print(mult_on_2(testlist))

print(list(map(mult_on_2, testlist)))