a=int(input())
b=int(input())
for i in range(a,b+1):
    j=str(i)
    if j==j[::-1]:
        print(j,end=" ")
    
    
    