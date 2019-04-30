# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    else:
        f = [1,1]
        i = 0
        for i in range(n-2):
            x = f[i] + f[i+1]
            i += 1
            f.append(x)
        return f[-1]

n = int(input())
print(calc_fib(n))
