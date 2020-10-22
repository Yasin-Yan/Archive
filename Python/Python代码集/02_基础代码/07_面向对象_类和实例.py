class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

if __name__ == '__main__':
    student = Student('YasinYan', 100)
    student.print_score()
    print(student.get_grade())