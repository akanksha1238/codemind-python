n=int(input())
a=list(map(int,input().split()))
s=0
cnt=0
for i in a:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s+=i
            cnt+=1
print("{:.2f}".format(s/cnt))