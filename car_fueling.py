# python3
import sys


def compute_min_refills(distance, tank, stops):
    stop = 0
    if distance <= tank:
        stop = 0
    else:
        dis = []
        s = len(stops)
        stops2 = stops
        stops2.append(distance)
        for i in range(s):
            d = stops2[i+1] - stops2[i]
            dis.append(d)
        dis.sort()
        if dis[-1] > tank:
            stop = -1
        else:
            for i in range(len(stops)):
                if distance > tank:
                    if stops[i] >= tank:
                        distance = distance - stops[i-1]
                        stop += 1
                    else:
                        continue
    return stop

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

