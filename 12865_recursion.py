import sys

n, k =map(int, sys.stdin.readline().split())

lst = []

for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    lst.append([a,b])
m = 0
result_v = []
result_w = []
def recursion():
    global m
    if sum(result_w) >k:
        return
    else:
        if sum(result_v) > m:
            m = sum(result_v)
    
    for i in range(n):
        if len(result_w)==0 or lst[i][0] not in result_w:
            result_v.append(lst[i][1])
            result_w.append(lst[i][0])
            recursion()
            result_v.pop()
            result_w.pop()

recursion()
print(m)