def like_or_dislike(lst):
    result = 'Nothing'
    for elem in lst:
        if elem == 'Like' and result == 'Like':
            result = 'Nothing'
        elif elem == 'Like' and result == 'Nothing':
            result = 'Like'
        elif elem == 'Like' and result == 'Dislike':
            result = 'Like'

        elif elem == 'Dislike' and result == 'Nothing':
            result = 'Dislike'
        elif elem == 'Dislike' and result == 'Dislike':
            result = 'Nothing'
        elif elem == 'Dislike' and result == 'Like':
            result = 'Dislike'
    return result

print(like_or_dislike(['Like', 'Like', 'Dislike', 'Like', 'Like']))