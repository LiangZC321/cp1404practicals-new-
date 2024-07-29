import random
from prac_09.car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.random() * 100 < self.reliability:
            return super().drive(distance)
        return 0