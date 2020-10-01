m,n = map(int,input().split())
n=(n)%60
if n <= 1:
    print(n)

else:

    previous = 0
    current  = 1
    sum=1
    for i in range(2,n):
        previous, current = current, (previous + current)%10
        if(n//60>m//60 and m%60>i):
            sum+=current

    print(sum%10)





