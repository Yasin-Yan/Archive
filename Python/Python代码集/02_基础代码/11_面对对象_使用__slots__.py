class Student(object):
    __slots__ = ('name', 'age') # 允许实例绑定的属性

if __name__ == '__main__':
    s = Student()
    s.name = 'Yasin@Yan'
    print(s.name)
    # s.score = 123
    # print(s.score)
