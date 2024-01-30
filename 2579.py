#dp

n = int(input())

lst=[]

for _ in range(n):
    x = int(input())
    lst.append(x)


result = []

for i in range(n):
    if i==0:
        result.append([lst[i], 0])
    elif i==1:
        result.append([lst[0]+lst[1], lst[1]])
    else:
        result.append([lst[i] + result[i-1][1] , lst[i] + max(result[i-2])])

print(max(result[-1]))