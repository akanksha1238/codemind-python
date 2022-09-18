n=int(input())
cnt1=0
cnt2=0
while n>0:
    r=n%10
    if r%2==0:
        cnt1+=1
    else:
        cnt2+=1
    n=n//10
if cnt1==0:
    print("Odd")
elif cnt2==0:
    print("Even")
else:
    print("Mixed")