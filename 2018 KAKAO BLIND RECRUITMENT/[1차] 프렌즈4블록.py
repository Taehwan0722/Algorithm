def solution(m, n, board):
    answer = 0
    r_board = list(map(list, zip(*board[::-1])))
    
    record = cycle(r_board)
    
    while record:
        answer += update(record, r_board)
        record = cycle(r_board)
        
    return answer

def cycle(board):
    record = set()
    for y in range(len(board) - 1):
        for x in range(len(board[y]) - 1):
            is_update = check(y, x, board)
            if is_update:
                record.update({(y + dy, x + dx) for dy in range(2) for dx in range(2)})
    return record if record else False

def check(y, x, board):
    confirm = [board[y + dy][x + dx] for dy in range(2) for dx in range(2) if 0 <= x + dx < len(board[y + dy])]
                
    return True if len(confirm) == 4 and len(set(confirm)) == 1 else False
    
def update(record, board):
    erase = [0] * len(board)
    for y, x in sorted(record):
        board[y].pop(x - erase[y])
        erase[y] += 1
    
    return sum(erase)