t,s,b = map(int,input().split())
c=2*t*s*b*512
tc=c//1024
print("{}KB".format(tc))