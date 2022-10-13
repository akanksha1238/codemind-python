import math
t=int(input())
for i in range(t):
    x=int(input())
    if(x >= 0):
        sr = int(math.sqrt(x))
        if (sr*sr) == x:
            print("True")
        else:
            print("False")
    