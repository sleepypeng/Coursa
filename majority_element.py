# Uses python3
import sys

def get_majority_element(a,n):
    a.sort()
    if a.count(a[int(n/2)]) > n/2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)

