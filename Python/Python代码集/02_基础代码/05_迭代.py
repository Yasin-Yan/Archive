from collections.abc import Iterable

# 判断是否是可迭代对象
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

d = {
    'a':1,
    'b':2,
    'c':3
}
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)

# 输出下标
for i, value in enumerate(['a', 'b', 'c', 'd']):
    print(i, value)

# tuple
for x, y in [(1, 2), (3, 4), (4, 5), (5, 6)]:
    print(x, y)