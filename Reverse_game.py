n=int(input())
l=list(map(str,input().split()))
k=[]
for i in l:
    k.append(int(i[::-1]))
print(*k)