# Uses python3
import sys

def gcd(a, b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        while a*b != 0:
            if a > b:
                a = a-b
            else:
                b = b - a
        return a+b

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))