n=int(input())
t=n*n
s=0
while t!=0:
    rem=t%10
    s=s+rem
    t=t//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")