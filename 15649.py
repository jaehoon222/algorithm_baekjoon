n, m = map(int,input().split())
lst = []

def backtracking():
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return

    for i in range(1, n+1):
        if i not in lst:
            lst.append(i)
            backtracking()
            lst.pop()


backtracking()