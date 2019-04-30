# Uses python3
import sys

def binary_search(a, o, n, x):
    if n < o:
        return -1
    mid = int(o + (n - o) / 2)
    
    if mid >= len(a):
        return -1
    
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a, o, mid - 1, x)
    else:
        return binary_search(a, mid+1, n, x)
        

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    o = 0
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, o, n, x), end = ' ')
