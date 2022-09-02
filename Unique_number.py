n=int(input())
v=str(n)
s=set(str(n))
if len(v)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")