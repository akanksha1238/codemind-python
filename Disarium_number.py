def length(n):
    l=0
    while(n!=0):
        l=l+1
        n=n//10
    return l
num=int(input())
rem=0
sum=0
len=length(num)
n=num
while(num>0):
    rem=num%10
    sum=sum+int(rem**len)
    num=num//10
    len=len-1
if(sum==n):
    print("True")
else:
    print("False")