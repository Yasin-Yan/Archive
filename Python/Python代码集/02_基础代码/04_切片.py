L = ['Mary', 'Jack', 'Bob', 'Thomas']
print(L[0:3]) # 取前3个元素
# 0可以省略
print(L[:3])
print(L[-2:])

LR = list(range(100))
print(LR[:10:2]) # 前10个数每两个取一个
print(LR[::5]) # 所有数每5个取一个
# print(LR[:]) # 原样复制

# tuple
print((0, 1, 2, 3, 4, 5)[:3])