import heapq

n = int(input())

result = []
heap = []
for _ in range(n):
    x = int(input())
    if x==0:
        if len(heap)==0:
            result.append(0)
        else:
            top = heapq.heappop(heap) [1]
            result.append(top)
    else:
        heapq.heappush(heap,(abs(x), x) )


for i in result:
    print(i)