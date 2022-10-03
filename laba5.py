######### 1 #########

######### 2 #########
# Вариант 10

import math

def f(x: float) -> float:
    return x ** 3 - math.cos(math.pi * x)
print(f"y = {f(float(input('x = ')))}")

# Вариант 6
import math

def f(x: float) -> float:
    return 2 ** x + x ** 2 - 1.15
print(f"y = {f(float(input('x = ')))}")

# Вариант 11
import math

def f(x: float) -> float:
    return math.sqrt(x) - math.cos(0.387*x)
print(f"y = {f(float(input('x = ')))}")
