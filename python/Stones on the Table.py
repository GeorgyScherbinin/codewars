# https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python

def solution(stones):
    result = 0
    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]: result += 1
    return result



print(solution("RGGRGBBRGRR"))
print(solution("RGBRGBRGGB"))
print(solution("RRRRGGGGBBBB"))