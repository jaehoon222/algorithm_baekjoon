#하노이탑 이동 순서(재귀)

n = int(input())

count = 0

#점화식 사용
def hanoi(a, b, n):
    if n==1:
        print(a, b)
        return
    hanoi(a, 6-a-b,  n-1)
    print(a, b)
    hanoi(6-a-b, b, n-1)

print(2**n - 1)
hanoi(1,3,n)