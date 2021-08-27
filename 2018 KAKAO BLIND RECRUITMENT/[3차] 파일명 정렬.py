import re

def solution(files):
    return sorted(files, key = lambda x:(find(x, 'head'), find(x, 'number')))

def find(string, name):
    dic = {'head':'[a-zA-Z .-]+', 'number':'[0-9]{1,5}'}
    if name == 'head':
        return re.search(dic[name], string).group().lower()
    else:
        return int(re.search(dic[name], string).group())