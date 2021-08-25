def solution(m, musicinfos):
    answer = []
    m = conv(m)
    
    for info in musicinfos:
        start, end, song, rhythm = info.split(',')
        playtime = time2min(start, end)
        
        rhythm = conv(rhythm)
        rhythm = rhythm * (playtime // len(rhythm)) + rhythm[:playtime % len(rhythm)]
        
        if m in rhythm:
            answer.append((song, playtime))

    answer.sort(key = lambda x:-x[1])
    
    return answer[0][0] if answer else '(None)'

def conv(string):
    for sound in 'CDFGA':
        string = string.replace(sound + '#', sound.lower())
        
    return string

def time2min(start, end):
    h1, m1 = map(int, start.split(':'))
    h2, m2 = map(int, end.split(':'))
    
    return (60 * int(m1 > m2) + m2 - m1) + 60 * (h2 - h1 - int(m1 > m2))