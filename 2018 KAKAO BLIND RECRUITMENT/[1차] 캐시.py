from queue import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([0] * cacheSize)
    
    for city in cities:
        answer += update(cache, city, cacheSize)
            
    return answer

def update(cache, city, cacheSize):
    city = city.lower()
    if city in cache:
        cache.remove(city)
        cache.appendleft(city)
        return 1
    else:
        cache.appendleft(city)
        if len(cache) > cacheSize:
            cache.pop()
        return 5