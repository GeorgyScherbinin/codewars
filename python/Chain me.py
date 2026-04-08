#https://www.codewars.com/kata/54fb853b2c8785dd5e000957

def chain(init_val, functions):
    result = init_val
    for function in functions:
        result = function(init_val)
        init_val = result

    return result

def add10(x): return x + 10
def mul30(x): return x * 30

print(chain(50, [add10, mul30]))
# returns 1800