# Stoke prices are given in array. Find for which duration I can buy and sell Shares to get maximum profit.
# if buy and sell once
# if buy and sell multiple times, the minimum times to get all the possible profit
from enum import Enum

class OperationType(Enum):
    Buy = 1
    Sale = -1

class Operation:
    def __init__(self, type, price, time):
        self.type = type
        self.price = price
        self.time = time

class Trend(Enum):
    Up = 1
    Down = -1
    Flat = 0

class Status(Enum):
    Full = 1
    Empty = 0

class StockOperator
    def __init__(self, stock_prices):
        self.stock_prices = stock_prices
        self.status = Status.Full

    def get_trend(self, time):
        if time == len(self.stock_prices):
            return Trend.Flat
        if self.stock_prices[time+1] > self.stock_prices[time]
            return Trend.Up
        elif self.stock_prices[time+1] < self.stock_prices[time]
            return Trend.Down
        else:
            return Trend.Flat

    def take_action(self, time, trend):
        if self.status == Status.Empty:
            if trend == Trend.Up:
                return Operation(OperationType.Buy, self.stock_prices[time], time)
        else:
            if trend == Trend.Down or time == len(self.stock_prices) -1:
                return Operation(OperationType.Sale, self.stock_prices[time], time)
        return None

    def apply_action(self, action):
        if action:
            if self.status == Status.Empty:
                self.status = Status.Full
            else:
                self.status = Status.Empty

    def get_max_profit_actions(self, stock_prices):
        actions = []
        for time, price in enumerate(stock_prices):
            trend = self.get_trend(time)
            action = self.take_action(time, trend)
            actions.append(action)
            self.apply_action(action)
        return actions



