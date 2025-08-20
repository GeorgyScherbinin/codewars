def reject(seq, predicate): 
    # result = []
    # for elem in seq:
    #     if not predicate(elem):
    #         result.append(elem)
    # return [elem for elem in seq if elem not in predicate]

    return [elem for elem in seq if not predicate(elem)]



# print(reject(['a', 1, 2, 3, 4], [1, 2]))

print(reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0))