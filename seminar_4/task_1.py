# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

import math
import random

precision_list = []
pi = math.pi
for i in range(-10, 0):
    precision_list.append(float(10**i))

precision = str(random.choice(precision_list))
if 'e' in precision:
    print(precision)
    k_round = int(precision[3:len(precision)])
    print(k_round)
    print(round(pi, k_round))
else:
    print(precision)
    p = precision[2:len(precision)]
    k_round = len(p)
    print(k_round)
    print(round(pi, k_round))


