# Uses python3
import sys

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

def lcm(a, b):
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    else:
        lcm = a * b // gcd(a, b)
        lcm = int(lcm)
        return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b)) 
