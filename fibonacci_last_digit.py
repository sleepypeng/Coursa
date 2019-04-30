# Uses python3
def last_digit(n):
    if n <= 1:
        return n
    else:
        f = [1,1]
        i = 0
        for i in range(n-2):
            x = f[i] + f[i+1]
            n,r = divmod(x,10)
            i += 1
            f.append(r)
        return f[-1]

n = int(input())
print(last_digit(n))