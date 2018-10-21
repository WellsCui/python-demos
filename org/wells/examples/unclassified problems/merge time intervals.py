# merge time intervals
class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

class Event:
    def __init__(self, time, event_type, interval):
        self.time = time
        self.event_type = event_type
        self.interval = interval


def build_time_line(intervals):
    events = []
    for interval in intervals:
        events.append(Event(interval.begin, "begin", interval) )
        events.append(Event(interval.end, "end", interval))
    events.sort(key=lambda p: p.time)
    return events


def join_interval(scr, dst):
    if scr.end > dst.end:
        dst.end = scr.end


def merge(intervals):
    events = build_time_line(intervals)
    rs = []
    current = None
    for event in events:
        if current is None:
            current = Interval(event.interval.begin, event.interval.end)
        elif event.time <= current.end:
            if event.event_type == "begin":
                join_interval(event.interval, current)
        else:
            rs.append(current)
            current = Interval(event.interval.begin, event.interval.end)
    if current:
        rs.append(current)
    return rs


def merge_test():
    ps = [(1, 5), (2, 6), (3, 6), (2, 5), (7, 15), (13, 25), (26, 29)]
    intervals = [Interval(begin, end) for begin, end in ps]
    new_intervals = merge(intervals)
    for item in new_intervals:
        print("begin: %s, end: %s" % (item.begin, item.end))


merge_test()



