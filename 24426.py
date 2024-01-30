n = int(input())

count1 = 0
count2 = 0

def fib1(n):
    global count1
    if n<=2:
        return 1
    else:
        count1+=1
        return fib1(n-1) + fib1(n-2)
    

lst = [1,1]
def fib2(n):
    global count2
    for i in range(2, n):
        count2+=1
        lst.append(lst[i-1] + lst[i-2])
    return lst[-1]
fib1(n)
fib2(n)
print(count1+1, count2)