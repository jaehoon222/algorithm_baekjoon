n = int(input())

lst = list(map(int, input().split()))

m = int(input())

result = list(map(int, input().split()))

lst.sort()


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
        print(1)
        return

for i in result:
    recursion(0, n-1, i)
