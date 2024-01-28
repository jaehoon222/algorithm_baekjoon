#터렛

import math
n = int(input())
l=[]
for i in range(n):

    a = list(map(int,input().split()))

    if a[2]>a[5]:
        max_num = a[2] #반지름 최댓값
        min_num=a[5]
    else:
        max_num=a[5]
        min_num= a[2]


    dis = math.sqrt((a[0]-a[3])**2 + (a[1]-a[4])**2)# 두점사이 거리

    if dis==0:
        if a[2]==a[5]:
            l.append(-1)
            continue
        else:
            l.append(0)
            continue

    if max_num<dis:#원밖
        if dis > a[2]+a[5]:
            l.append(0)
            continue
        elif dis ==a[2]+a[5]:
            l.append(1)
            continue
        else:
            l.append(2)
            continue
    elif max_num>dis:#원안
        if max_num>min_num+dis:
            l.append(0)
            continue
        elif max_num==min_num+dis:
            l.append(1)
            continue
        else:
            l.append(2)
            continue
    else:
        l.append(2)
        continue
for i in l:
    print(i)