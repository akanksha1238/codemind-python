t=int(input())
for i in range(t):
    n=int(input())
    a=n
    b=n
    while True:
        is_prime=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
             a=a-1
    while True:
        is_prime=True
        for i in range(2,int(b**0.5)+1):
            if b%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
             b=b+1
    c=min(a,b)
    if(abs(n-a)>abs(b-n)):
        print(b)
    else:
        print(a)