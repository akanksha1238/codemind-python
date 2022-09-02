n=int(input())
li=list(map(int,input().split()))
c=0
for i in range(n):
    if i==0:
        if (li[-1]%2==0 and li[i+1]%2==1) or (li[-1]%2==1 and li[i+1]%2==0):
            c+=1
    elif i!=n-1:
        if (li[i-1]%2==0 and li[i+1]%2==1) or (li[i-1]%2==1 and li[i+1]%2==0):
            c+=1
    else:
        if (li[i-1]%2==0 and li[0]%2==1) or (li[i-1]%2==1 and li[0]%2==0):
            c+=1
print(c)