import random
import math
from typing import List

def circarea(radius: float) -> float:
    return math.pi * radius ** 2

def averscore(scores: List[int]) -> float:
    return sum(scores) / len(scores)

def sber(money: float, stock_price: float) -> int:
    return math.floor(money / stock_price)
