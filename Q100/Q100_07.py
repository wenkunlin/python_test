xy = input('请输入x,y:').split(',')
print(xy)
result = list()
for i in range(0,int(xy[0])):
    m = list()
    for n in range (0,int(xy[1])):
        m.append(i * n)
    result.append(m)
print(result)

