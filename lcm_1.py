# Uses python3
import sys

def lcm(a, b):    
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    else:
        A = a
        B = b
        while a*b != 0:
            if a > b:
                a = a-b
            else:
                b = b - a
        gcd = a+b
        lcm = A * B / gcd
        lcm = int(lcm)
        return lcm
        
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
