l = list(map(int,input().split()))
num = 0
for i in range(len(l)):
    c = 0
    fmin = l[i]
    for p in range(len(l[i:])):
        if fmin > l[p]:
            fmin = l[p]
            num = p
            c = 1
    if c == 1:
        l[num] = l[i]
        l[i] = fmin
print(l)
