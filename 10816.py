import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
result = list(map(int, sys.stdin.readline().split()))

lst = sorted(lst)



def chech_num(idx, m):
    count = -1

    for i in range(idx, -1, -1):
        if lst[i]==m:
            count+=1
        else:
            break

    for i in range(idx, len(lst)):
        if lst[i]==m:
            count+=1
        else:
            break

    return count

def recursion(first_idx, last_idx, i):
    if first_idx >last_idx:
        print(0)
        return
    

    mid = (last_idx +  first_idx)//2

    if lst[mid] < i:
        recursion(mid+1, last_idx, i)
    elif lst[mid] > i:
        recursion(first_idx, mid-1, i)
    else:
        print(chech_num(mid, i))
        return

for i in result:
    recursion(0, n-1, i)
