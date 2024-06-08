def rec(n):
    if n==0:
        return
    else:
        print(n)
    return rec(n-1)
d=int(input())
print(rec(d))