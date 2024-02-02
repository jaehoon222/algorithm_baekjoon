n, m = map(int, input().split())

lst = []

for _ in range(n):
    x = int(input())
    lst.append(x)

count = 0

for i in range(n-1, -1, -1):
    while(lst[i] <=m):
        count+=1
        m-=lst[i]

    if m==0:
        break

print(count)