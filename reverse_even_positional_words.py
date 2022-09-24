s=list(map(str,input().split()))
cnt=0
for i in s:
    cnt+=1
    if cnt%2==1:
        rev=i[::-1]
        print(rev,end=" ")
    else:
        print(i,end=" ")