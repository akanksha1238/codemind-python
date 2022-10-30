n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(100):
    for j in l:
        if i*i==j:
            s+=j
print(s)