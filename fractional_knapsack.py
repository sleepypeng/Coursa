# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0
    n = len(weights)
    i = 0
    l = [0] * n
    for i in range(n):
        l[i] = values[i] / weights[i]
        i += 0
    b = np.argsort(l)
    m = b.tolist()
    m.reverse()
    while capacity > 0:
        if capacity >= weights[m[0]]:
            value += values[m[0]]
            capacity -= weights[m[0]]
        elif capacity < weights[m[0]]:
            value += capacity * values[m[0]] / weights[m[0]]
            capacity = 0
        else:
            print("capacity is wrong")
        del m[0]
        if len(m) == 0:
            break
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
