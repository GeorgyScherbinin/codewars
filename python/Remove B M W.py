# https://www.codewars.com/kata/59de795c289ef9197f000c48/train/python
def remove_bmw(string):
    print(type(string))
    if isinstance(string, str):
        output_list = []
        bmwlist = ['B', 'M', 'W']
        for word in string:
            if word.upper() not in bmwlist:
                output_list.append(word)
        return ''.join(output_list)
    else:
        raise TypeError("This program only works for text.")
        return (f"{string}")

print(remove_bmw('5m46w5b1'))