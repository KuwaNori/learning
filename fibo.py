def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


p = int(input())

memo = [-1 for i in range(1000)]

print(fibo(p))
print(memo)
