#https://www.codewars.com/kata/54fb853b2c8785dd5e000957

def chain(init_val, functions):
    result = 0
    for function in functions:
        result += function(init_val)

    return result

def mul30(x): return x * 30
def add10(x): return x + 10


print(chain(50, [add10, mul30]))
# returns 1800