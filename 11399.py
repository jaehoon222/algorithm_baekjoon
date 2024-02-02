n = int(input())

lst = list(map(int, input().split()))

lst.sort()

result = 0
l = len(lst)
for i in range(len(lst)):
    result += (l-i)*lst[i]

print(result)