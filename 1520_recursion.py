import sys

n, m = map(int, sys.stdin.readline().split())

lst = []

for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    lst.append(x)

dp = [[0,0]]
count = 0
idx = [[1, 0], [0, 1], [-1, 0], [0,-1]]
def recursion():
    global count
    if dp[-1] == [n-1, m-1]:
        count+=1
        return

    x = dp[-1]
    for i in idx:
        if n-1>=x[0] + i[0] and x[0] + i[0] >=0 and m-1>=x[1] + i[1] and x[1] + i[1] >=0:
            if lst[x[0] + i[0]][x[1] + i[1]] < lst[x[0]][x[1]]:
                dp.append([x[0] + i[0], x[1] + i[1]])
                recursion()
                dp.pop()
    
recursion()
print(count)
