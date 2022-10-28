def isPrime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
                break
        return True
num=int(input())
c=0
for i in range(1,num+1):
    if num%i==0 and isPrime(i)==False:
        c+=1
print(c)
    