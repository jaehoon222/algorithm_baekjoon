import sys
input = sys.stdin.readline().strip()

a, b, c = map(int, input.split())


def recursion(x):
    if x==1:
        return a
    if x%2==0:
        return (recursion(x//2)**2) %c
    else:
        return (recursion(x-1) * a) %c
    
print(recursion(b)%c)