for t in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    o=0
    for i in v:
        if i%2:
            o+=1
    print(o//2)