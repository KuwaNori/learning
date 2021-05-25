# 絶対値を返す関数を定義
def check(a,b):
    c = max(a,b)
    d = min(a,b)
    return c-d

# ポールの数の入力
n = int(input())

# n個それぞれの高さの受け取り
trees = list(map(int, input().split()))

# 配列shortestを用意（0番目への到達最小コストの0をindex0する）
shortest = [0]

# 配列shortestにそれぞれのポールへの最小コストを入れて行くループ
for i in range(1,n):
    if i == 1:
        # iが1の時は最小コストが0からの場合のみなので 0番目と1番目のさを代入
        result = check(trees[0],trees[1])
        shortest.append(result)

    else:
        # min( i-1番目への最小コスト + i-1番目とi番目の差, i-2番目への最小コスト + i-2番目とi番目の差)
        result = min(shortest[i-1]+check(trees[i-1],trees[i]),shortest[i-2]+check(trees[i-2],trees[i]))

        # i番目への最小コストを代入
        shortest.append(result)

    print(shortest)
# 最後の結果shortestのn-1番目の結果を出力
print(shortest[n-1])

# 計算量はＯ(2N)だと思う
