n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [0]
x = 0
for i in lst:
    x+=i
    sum_lst.append(x)

for i in range(m):
    a, b = map(int, input().split())
    print(sum_lst[b] - sum_lst[a-1])
