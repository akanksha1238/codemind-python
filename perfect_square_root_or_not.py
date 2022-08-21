from math import sqrt
n = int(input())
sq_root = int(sqrt(n))
if sq_root*sq_root==n:
    print("True")
else:
    print("False")