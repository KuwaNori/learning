box = list(map(int, input().split()))
target = int(input())
for i in box:
    if i == target:
        print("Yes")
        exit()
print("No")
