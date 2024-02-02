import sys
input = sys.stdin.readline

n = int(input())

fin_time = 0
count = 0
lst = []

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a,b])

lst.sort()
lst.sort(key=lambda x: x[1])
for i in lst:
    if i[0] >=fin_time:
        fin_time = i[1]
        count+=1

print(count)