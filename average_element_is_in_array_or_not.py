n = int(input())
t = list(map(int,input().split()))
s=sum(t)
avg=s//n
if avg in t:
    print("True")
else:
    print("False")
