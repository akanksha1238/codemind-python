n=int(input())
l=list(map(str,input().split()))
s=0
for i in l:
    for k in i:
        s=s+int(k)
print(s)