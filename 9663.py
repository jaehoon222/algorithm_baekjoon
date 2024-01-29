n = int(input())
count = 0
lst = []

def check_kill(idx, k):
    for i in range(idx):
        if k == lst[i]  or abs(lst[i] - k) == abs(idx-i):
            return False
    return True

def backtracking(x):
    global count
    if x==n:
        count +=1
        return
    
    for i in range(n):
        if check_kill(x, i): #앞놈까지의 index, 넣을 값
            lst.append(i)
            backtracking(x+1)
            lst.pop()


backtracking(0)
print(count)