from math import pi
from .core import Parameterization

class FooParameterization(Parameterization):
    def volume(self, radius):
        return (4/3) * pi * radius**3
