n = int(input())


lst = []

for i in range(n):
    x = list(map(int, input().split()))
    lst.append(x)

result = []
result.append(lst[0])
for i in range(n-1):
    result.append([min(result[i][2], result[i][1]) + lst[i+1][0], min(result[i][0], result[i][2]) + lst[i+1][1], min(result[i][0], result[i][1]) + lst[i+1][2]] )
print(min(result[-1]))