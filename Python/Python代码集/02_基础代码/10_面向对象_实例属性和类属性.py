class Student(object):
    name = 'Yasin@Yan'

if __name__ == '__main__':
    s = Student()
    s.score = 97

    print('%s: %s' % (s.name, s.score))