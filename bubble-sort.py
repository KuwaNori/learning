box = list(map(int, input().split()))
k = 1
#昇順に並び替え
for i in range(len(box)-1):
    while True:
        first = box[i]
        second = box[i+k]
        if first > second:
            box[i+k] = first
            box[i] = second
        k+=1
        if i+k == len(box):
            k = 1
            break
print(box)
