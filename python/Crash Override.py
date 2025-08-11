# https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python

#from preloaded import FIRST_NAME, SURNAME

def alias_gen(f_name: str, l_name: str) -> str:
    return  FIRST_NAME[f_name[0].capitalize()] + ' ' + SURNAME[l_name[0].capitalize()] if f_name[0].isalpha() and l_name[0].isalpha() else 'Your name must start with a letter from A - Z.'

#alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'

print(alias_gen('123abc', 'Petrovic'))