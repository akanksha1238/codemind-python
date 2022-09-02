m=int(input())
n=abs(m)
rev=0
while n>0 or n<0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if m<0:
    print(rev*-1)
else:
    print(rev)