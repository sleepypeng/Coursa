def last_dig(n):
    if (n <= 1):
        return n

    else:
        f=0
        s=1
        temp=f+s
        sum=1
        for i in range(1,n):
            temp=f+s
            f=s
            s=temp
            sum+=temp*temp
        return sum%10
n = int(input())
print(last_dig(n))
