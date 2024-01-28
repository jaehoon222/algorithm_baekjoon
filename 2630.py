#색종이 만들기
import sys

n = int(sys.stdin.readline().strip())
paper = []

for i in range(n):
    x = list(map(int, sys.stdin.readline().strip().split()))
    paper.append(x)

blue = 0
white = 0

def sum_list(x):
    num = 0
    for j in x:
        n = sum(j)
        num+=n
    return num

def cut(n, paper):
    global blue
    global white

    rows = len(paper)
    cols = len(paper[0])

    if n==1:
        return
    
    x1 = [row[:cols // 2] for row in paper[:rows // 2]]
    x2 = [row[cols // 2:] for row in paper[:rows // 2]]
    x3 = [row[:cols // 2] for row in paper[rows // 2:]]
    x4 = [row[cols // 2:] for row in paper[rows // 2:]]
    if sum_list(x1)==(n/2)**2:
        blue +=1
    elif sum_list(x1)==0:
        white+=1
    else:
        cut(n//2, x1)


    if sum_list(x2)==(n/2)**2:
        blue+=1
    elif sum_list(x2)==0:
        white+=1
    else:
        cut(n//2, x2)


    if sum_list(x3)==(n/2)**2:
        blue+=1
    elif sum_list(x3)==0:
        white+=1
    else:
        cut(n//2, x3)


    if sum_list(x4)==(n/2)**2:
        blue+=1
    elif sum_list(x4)==0:
        white+=1
    else:
        cut(n//2, x4)


if sum_list(paper)== n*n:
    blue+=1
elif sum_list(paper)==0:
    white+=1
else:
    cut(n, paper)
    
print(white)
print(blue)