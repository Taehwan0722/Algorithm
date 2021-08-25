import re

def solution(dartResult):
    scores = re.findall('[0-9]+[STD][*#]*', dartResult)
    
    record = [0] * 3
    
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'*':2, '#':-1}
    
    for idx, score in enumerate(scores):
        s = int(re.search('[0-9]+', score).group())
        b = bonus[re.search('[SDT]', score).group()]
        o = re.search('[*#]', score)
        
        record[idx] = s ** b
        
        if o:
            o = option[o.group()]
            record[idx] = record[idx] * o
            if o == 2 and idx > 0:
                record[idx - 1] *= o
        
    return sum(record)