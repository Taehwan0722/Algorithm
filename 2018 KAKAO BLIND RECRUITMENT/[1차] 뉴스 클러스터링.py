import re
from collections import Counter

def solution(str1, str2):
    c_str1 = Counter(convert(str1))
    c_str2 = Counter(convert(str2))
    
    return J(c_str1, c_str2)

# \W에는 _가 포함되지 않아 따로 추가해줘야한다. (\w에는 _ 포함)
def convert(string):
    return [string[i:i+2].lower() for i in range(len(string) - 1) if not re.search('[\W0-9_]', string[i:i+2])]

def J(str1, str2):
    inter = str1 & str2
    union = str1 | str2
    
    inter_cnt = sum(value for value in inter.values())
    union_cnt = sum(value for value in union.values())
    
    if union_cnt:
        return int(inter_cnt / union_cnt * 65536)
    else:
        return 65536