def isPrime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
                break
        else:
            return True
a=int(input())
b=int(input())
n1=a+b+1
n2=a+b
while True:
    if isPrime(n1)==True:
        print(n1-n2)
        break
    else:
        n1+=1

        