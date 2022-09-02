n=int(input())
c=len(str(n))
sq=n**2
id=sq%pow(10,c)
if id==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")