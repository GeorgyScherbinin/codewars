# https://www.codewars.com/kata/57a4d500e298a7952100035d

def hex_to_dec(s):
    s = s.upper()

    hex_dict = {'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    dec_res = 0
    step = len(s) - 1 #123

    for digit in s:
        dec_res += hex_dict[digit] * 16**step
        step -= 1
    return dec_res

print('')
print(hex_to_dec('e12ef'))