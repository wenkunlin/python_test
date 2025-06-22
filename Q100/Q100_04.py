#输入数字
n = input('请输入一系列数字以逗号分隔：')
list = n.split('，',)
tuple = tuple(list)
# 打印列表
print(list)
# 打印元组
print(tuple)