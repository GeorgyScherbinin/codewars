string = 'testofiteration123456789'
for word, slice in zip(string, string[1:]):
    print(word, slice)

for word in string:
    print(word)
    
print(list(zip(string, string[1:])))