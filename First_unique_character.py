def fun(s):
    for i in s:
        if s.count(i)==1:
            return i
    return -1
s=input()
s1=s.lower()
s2=s1.replace(" ","")
print(fun(s2))