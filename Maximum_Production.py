

x= int(input())
lst= []
for i in range(x):
    y = list(map(int, input().split()))
    lst.append(y)
llst = []
for i in range(len(lst)):
    xx = 7 * lst[i][1]
    b = 7 - lst[i][0]
    xy = (lst[i][2] * lst[i][0]) + (lst[i][3] * b)

    if (xx > xy):
        llst.append(xx)
    else:
        llst.append(xy)

for i in llst:
    print(i)

