# import random
box = list(map(int, input().split()))
# box = [random.randrange(100000) for i in range(1000000) ]
target = int(input())
box = sorted(box)
count = 0
while True:
    count+=1
    if box[int(len(box)/2)] == target:
        print("Yes")
        break
    if box[int(len(box)/2)] > target:
        box = box[:int(len(box)/2)]
    else:
        box = box[int(len(box)/2):]
    if len(box) == 1 and box[0] != target:
        print("No")
        break
