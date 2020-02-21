'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word: str):
    if 'th' not in word:
        return 0

    one_th_removed = word.replace('th', '_', 1)
    return 1 + count_th(one_th_removed)
