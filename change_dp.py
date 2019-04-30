# Uses python3
import sys

def init(m):
    
    global cache
    global values
    
    values = [1, 3, 4]
    cache = [-1] * (m + 1)



def get_change(m):
    
    global cache
    global values
    
    min_coin = m
    
    if cache[m] != -1:
        min_coin = cache[m]
    elif m < 1:
        min_coin = 0
    elif m in values:
        min_coin = 1
    else:
        for x in [i for i in values if i <= m]:
            coinnum = 1 + get_change(m - x)
            if coinnum < min_coin:
                min_coin = coinnum
    cache[m] = min_coin
    return min_coin

if __name__ == '__main__':
    m = int(sys.stdin.read())
    init(m)
    print(get_change(m))

