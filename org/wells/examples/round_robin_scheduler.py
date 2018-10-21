
"""
Implement a round robin scheduler.
Each process has an arrival time Atime[i], execute time Etime[i].
Q is the maximum time that a process gets executed in its turn. If the process isn't finished after q, it waits till the next round.
Output average wait time for the processes.
"""
from datetime import datetime, timedelta
from time import sleep


class Process:
    def __init__(self, process_id, arrival_time, execute_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.execute_time = execute_time

    def execute(self, consume_time):
        print('process %s is executing for %d seconds' % (self.process_id, consume_time))
        sleep(consume_time)
        self.execute_time -= consume_time
        if self.execute_time == 0:
            print('process %s finished' % self.process_id)


class RoundRobinScheduler:
    def __init__(self, processes, slot_time):
        self.slot_time = slot_time
        processes.sort(key=lambda p: p.arrival_time)
        self.processes = processes
        self.waiting_queue = []

    @staticmethod
    def wait_start(start_time):
        if start_time <= datetime.now():
            return
        else:
            interval = start_time - datetime.now()
            sleep(interval.seconds)

    def get_next_process(self):
        if len(self.waiting_queue) == 0:
            return self.processes.pop(0)
        elif len(self.processes) == 0:
            return self.waiting_queue.pop(0)
        elif self.processes[0].arrival_time <= datetime.now():
            return self.processes.pop(0)
        else:
            return self.waiting_queue.pop(0)

    def execute_process(self, process):
        if process.execute_time <= self.slot_time:
            process.execute(process.execute_time)
        else:
            process.execute(self.slot_time)
            self.waiting_queue.append(process)

    def start(self):
        while len(self.processes) > 0 or len(self.waiting_queue) > 0:
            process = self.get_next_process()
            self.wait_start(process.arrival_time)
            self.execute_process(process)


def test_scheduler():
    ps = [(1, 5), (2, 6), (10, 3), (4, 3), (15, 15), (13, 8), (16, 9)]
    processes = [Process(process_id,
                         datetime.now() + timedelta(seconds=start),
                         interval)
                 for process_id, (start, interval)
                 in enumerate(ps)]

    scheduler = RoundRobinScheduler(processes, 3)
    scheduler.start()


test_scheduler()
