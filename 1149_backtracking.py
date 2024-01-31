#backtracking 시간초과남

n = int(input())

lst = []

for i in range(n):
    x = list(map(int, input().split()))
    lst.append(x)

mini = 10000
result = []

def recursion(l, idx):
    global mini
    if l==n:
        if sum(result)<mini:
            mini=sum(result)
    else:
        for i in range(3):
            if i!=idx:
                result.append(lst[l][i])
                recursion(l+1, i)
                result.pop()

recursion(0,4)
print(mini)