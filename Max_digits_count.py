n=int(input())
a=list(map(int,input().split()))
ls=[]
cnt1=0
for i in a:
    cnt=0
    while i>0:
        r=i%10
        cnt+=1
        i=i//10
    ls.append(cnt)
l=max(ls)
for i in ls:
    if i==l:
        cnt1+=1
print(cnt1)
