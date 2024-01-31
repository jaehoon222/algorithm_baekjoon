n = int(input())

lst = []
for i in range(n):
    lst.append([0,0,0,0,0,0,0,0,0,0])

lst[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, n):
    for j in range(10):
        if j==0:
            lst[i][0] += lst[i-1][1]
        elif j==9:
            lst[i][9] += lst[i-1][8]
        else:
            lst[i][j] += lst[i-1][j-1] + lst[i-1][j+1]



print(sum(lst[-1])%1000000000)