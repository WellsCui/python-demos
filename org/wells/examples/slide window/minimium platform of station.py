"""
Minimum Number of Platforms Required for a Railway/Bus Station
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)
"""
from enum import Enum
from dateutil import parser


class BusSchedule:
    def __init__(self, bus, arrival, departure):
        self.bus = bus
        self.arrival = arrival
        self.departure = departure


class BusEvent:
    def __init__(self, bus, event_time, event_type):
        self.bus = bus
        self.event_time = event_time
        self.event_type = event_type


class EventType(Enum):
    ARRIVAL = 0
    DEPARTURE = 1


class Solution:

    def build_events(self, schedules):
        for schedule in schedules:
            yield BusEvent(schedule.bus, schedule.arrival, EventType.ARRIVAL)
            yield BusEvent(schedule.bus, schedule.departure, EventType.DEPARTURE)

    def resolve(self, schedules):

        buses_in_station = []
        buses_in_station_count = 0
        max_buses_in_station = 0

        def handle_event(evt):
            nonlocal buses_in_station_count
            nonlocal max_buses_in_station
            if evt.event_type == EventType.ARRIVAL:
                buses_in_station.append(evt.bus)
                buses_in_station_count += 1
            else:
                buses_in_station.remove(evt.bus)
                buses_in_station_count -= 1
            if buses_in_station_count > max_buses_in_station:
                max_buses_in_station = buses_in_station_count

        events = [e for e in self.build_events(schedules)]
        events.sort(key=lambda e: e.event_time)
        for event in events:
            handle_event(event)

        print(max_buses_in_station)


def test_solution():
    times = [('09:00', '09:10'), ('09:40', '12:00'), ('09:50', '11:20'),
             ('11:00', '11:30'), ('15:00', '19:00'), ('18:00', '20:00')]
    schedules = [BusSchedule("bus-{0}".format(bus), parser.parse(arrival), parser.parse(departure))
                 for bus, (arrival, departure) in enumerate(times)]
    Solution().resolve(schedules)


test_solution()
