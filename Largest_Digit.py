n = int(input())
max=0
while(n!=0):
    lar=n%10
    if max<lar:
        max=lar
    n=n//10
print(max)

