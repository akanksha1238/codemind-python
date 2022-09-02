def rd(n):
    r=0
    while n>0:
        r=r*10+n%10
        n=n//10
    return r
def sq(n):
    return (n*n)
def adam(n):
    a=sq(n)
    b=sq(rd(n))
    if a==rd(b):
        return True
    else:
        return False
n=int(input())
if adam(n):
    print("True")
else:
    print("False")