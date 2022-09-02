import math
n=int(input())
sr=(int)(math.sqrt(n))
if sr*(sr+1)==n:
    print("YES")
else:
    print("NO")