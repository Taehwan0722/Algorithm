def solution(n, t, m, timetable):
    bus = {540 + i * t:[] for i in range(n)}
    timetable = sorted(map(time2min, timetable), reverse=True)
    board(timetable, bus, t, m)
    
    if len(bus[540 + (n - 1) * t]) != m:
        return min2time(540 + (n - 1) * t)
       
    return find_time(bus)

def time2min(time):
    h, m = map(int, time.split(':'))
    return 60 * h + m

def min2time(m):
    return f'{m // 60}'.zfill(2) + ':' + f'{m % 60}'.rjust(2, '0')

def board(timetable, bus, t, m):
    bus_time = 540
    while bus_time in bus:
        while timetable and timetable[-1] <= bus_time and len(bus[bus_time]) != m:
            bus[bus_time].append(timetable.pop())
        bus_time += t
            
def find_time(bus):
    times = sum(bus.values(), [])[::-1]
    for i in range(len(times) - 1):
        if times[i] - times[i + 1] > 0:
            return min2time(times[i] - 1)
    return min2time(times[-1] - 1)