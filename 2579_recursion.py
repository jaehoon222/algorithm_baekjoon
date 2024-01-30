#재귀(시간초과)

n = int(input())

lst=[]

for _ in range(n):
    x = int(input())
    lst.append(x)


m = 0
distance = []
result = []
def recursion():
    global m
    if sum(distance) ==n:
        if sum(result) > m:
            m = sum(result)
        return
    else:
        idx = sum(distance)

        # print(distance)

        for i in range(idx, idx+2):

            if sum(distance)+(i-idx+1) <=n:
                if idx<=1:
                    distance.append(i-idx+1)
                    result.append(lst[i])
                    recursion()
                    distance.pop()
                    result.pop()
                else:
                    if distance[-1]==1 and idx!=i:
                        distance.append(i-idx+1)
                        result.append(lst[i])
                        recursion()
                        distance.pop()
                        result.pop()
                    elif distance[-1]==2:
                        distance.append(i-idx+1)
                        result.append(lst[i])
                        recursion()
                        distance.pop()
                        result.pop()



recursion()
print(m)