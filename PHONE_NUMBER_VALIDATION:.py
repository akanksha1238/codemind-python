n=int(input())
d=rev=0
while n>0:
    rem=n%10
    d+=1
    rev=rev*10+rem
    n=n//10
if rev%10!=0 and d==10:
    print("Valid")
else:
    print("Invalid")
    