def solution(n, t, m, p):
    record = []
    number = 0
    
    while len(record) // m < t:
        s = convert(number, n, [])
        number += 1
        record.extend(s)
    
    return ''.join(record[p-1::m][:t])

def convert(number, n, s=[]):
    numbers = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    if number // n == 0:
        s.append(f'{number}' if number < 10 else f'{numbers[number]}')
        return s
    
    convert(number // n, n, s)
    over10 = number % n
    s.append(f'{over10}' if over10 < 10 else f'{numbers[over10]}')
    return s