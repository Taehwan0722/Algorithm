def solution(record):
    answer = []
    nickname = {}
    
    for log in record:
        log = log.split()
        if log[0] == 'Enter':
            get_in(log, nickname, answer)
        elif log[0] == 'Leave':
            get_out(log, nickname, answer)
        else:
            change_name(log, nickname)
    
    return list(map(lambda x:nickname[x[0]].name + x[1], answer))

def get_in(log, nickname, answer):
    if log[1] not in nickname:
        nickname[log[1]] = nick(log[2])
    else:
        nickname[log[1]].name = log[2]
    answer.append([log[1], '님이 들어왔습니다.'])
    
def get_out(log, nickname, answer):
    answer.append([log[1], '님이 나갔습니다.'])

def change_name(log, nickname):
    nickname[log[1]].name = log[2]
    
class nick:
    def __init__(self, name):
        self.name = name