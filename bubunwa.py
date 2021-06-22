def check(i,w,a):
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    if check(i-1, w, a):
        return True
    if check(i-1, w-a[i-1], a):
        return True
    return False



w = int(input())
l = list(map(int, input().split()))
if check(len(l), w, l):
    print("Yes")
else:
    print("No")
