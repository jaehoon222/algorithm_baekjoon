n, k =map(int, input().split())

dp = [0 for _ in range(k+1)]

lst = []
for i in range(n):
    a, b = list(map(int, input().split()))
    lst.append([a,b])



for item in lst:
    w, v = item
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)

print(max(dp))