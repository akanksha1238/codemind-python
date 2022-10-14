t=int(input())
for i in range(t):
    n=int(input())
    t=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if rev==t:
        print("True")
    else:
        print("False")