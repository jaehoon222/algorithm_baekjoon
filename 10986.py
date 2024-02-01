import sys

input = sys.stdin.readline().strip()

n, m = map(int, input.split())

input = sys.stdin.readline().strip()
lst = list(map(int, input.split()))
count = 0

dp = [0 for _ in range(m)]
idx = lst[0]%m
dp[idx] = 1
if idx==0:
    count+=1

for i in range(1, len(lst)):
    x = dp.copy()
    idx = lst[i]%m
    for j in range(m):
        dp[(idx+j)%m] = x[j]
    dp[idx] +=1
    count += dp[0]        


print(count)