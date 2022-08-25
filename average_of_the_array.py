n = int(input())
t = list(map(int,input().split()))
s=sum(t)
avg=s/n
print("{:.2f}".format(avg))