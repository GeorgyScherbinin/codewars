# https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python
def validate_hello(greetings):
    #your code here
    dict_string = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    # words = greetings.split()
    # for word in words:
    #     if word.lower().replace('!','').replace('?','').replace('.','').replace(',','').replace(';','').replace(':','') in dict_string:
    #         return True
    # return False
    for word in greetings.split():
        for test_word in dict_string:
            if test_word in word.lower():
                return True
    return False

print(validate_hello('Hallo?!!! guys'))
