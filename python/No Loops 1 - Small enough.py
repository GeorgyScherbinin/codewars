# https://www.codewars.com/kata/57cc4853fa9fc57a6a0002c2
# 2

def small_enough(a, limit,): 
    if len(a) == 0: 
        return True
    else:
        if a[0] <= limit:
            a.pop(0)
            return small_enough(a, limit)
        else:
            return False
    


print(small_enough([78, 110, 110, 99, 104, 117, 107, 115], 116))
