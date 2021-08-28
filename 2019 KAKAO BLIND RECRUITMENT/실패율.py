from collections import Counter, defaultdict

def solution(N, stages):
    answer = [i for i in range(1, N + 1)]
    # 시간복잡도 O(n^2)
    # progress, arrived = get_count(stages)
    # return sorted(answer, key=lambda x:-get_fail_ratio(x, progress, arrived))
    
    # 시간복잡도 O(nlogn)
    fail_ratio = get_ratio(stages, N)
    return sorted(answer, key=lambda x:-fail_ratio[x])

def get_count(stages):
    progress = defaultdict(int)
    arrived = defaultdict(int)
    
    for stage in stages:
        for i in range(1, stage + 1):
            arrived[i] += 1
        progress[stage] += 1
            
    return progress, arrived

def get_ratio(stages, n):
    fail_ratio = defaultdict(int)
    arrived = len(stages)
    cnt = Counter(stages)
    
    for stage in sorted(cnt):
        fail_ratio[stage] = cnt[stage] / arrived
        arrived -= cnt[stage]
        
        if arrived == 0:
            return fail_ratio
        
    return fail_ratio

def get_fail_ratio(stage, progress, arrived):
    return progress[stage] / arrived[stage] if arrived[stage] != 0 else 0