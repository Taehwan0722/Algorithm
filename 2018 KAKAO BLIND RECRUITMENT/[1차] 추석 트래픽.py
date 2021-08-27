from queue import deque

def solution(lines):
    answer = 0
    # new_lines = sorted(map(convert, lines), key = lambda x:(x[1], x[0]))
    new_lines = sorted(map(convert, lines), key = lambda x:(-x[0], -x[1]))
    
    times = sorted(sum(new_lines, []))
    
    # print(new_lines)
    print(new_lines[::-1])
    
    
    record = deque()
    
    for time in times:
        while new_lines and new_lines[-1][0] < time + 1000:
            record.append(new_lines.pop())
        record.sort(key = lambda x:())
        while record and record[0][1] < time:
            record.popleft()
        print(time, record)
        if answer < len(record):
            answer = len(record)
        # answer = max(answer, len(record))
        
    # for start, end in new_lines:
    #     while record and start >= record[0][1] + 1000:
    #         record.popleft()
    #     record.append((start, end))
    #     if answer < len(record):
    #         answer = len(record)
    #         print(record)
    #     # answer = max(answer, len(record))
    
    return answer

def convert(string):
    date, end, length = string.split()
    return find_start(end, length[:-1])
    
def find_start(time, sec):
    h, m, s = time.split(':')
    s = 3600000 * int(h) + 60000 * int(m) + int(s.replace('.', ''))
    
    sec = int(sec.replace('.', '').ljust(4, '0'))

    return [s - sec + 1, s]