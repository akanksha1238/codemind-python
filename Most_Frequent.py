from collections import *
n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=0
for k,v in d.items():
    if v>m:
        m=v
for k,v in d.items():
    if v==m:
        print(k)
        break