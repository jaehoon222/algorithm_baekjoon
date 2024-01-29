n, m = map(int,input().split())
lst = []
result_lst = []

def backtracking():
    if len(lst) == m:
        sort_lst = sorted(lst)
        if sort_lst in result_lst:
            return
        else:
            result_lst.append(sort_lst)
            print(" ".join(map(str, lst)))
            return
        
    for i in range(1, n+1):
        if i not in lst:
            lst.append(i)
            backtracking()
            lst.pop()


backtracking()