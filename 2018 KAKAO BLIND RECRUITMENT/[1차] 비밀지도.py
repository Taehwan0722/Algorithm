from functools import partial

def solution(n, arr1, arr2):
    answer = [a | b for a, b in zip(arr1, arr2)]
    answer = list(map(partial(change, n=n), answer))
    
    return answer

def change(x, n):
    table = str.maketrans('10', '# ')
    return bin(x)[2:].zfill(n).translate(table)