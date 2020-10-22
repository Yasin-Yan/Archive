from enum import Enum, unique

# 默认
# Group = Enum('Group', ('A', 'B', 'C', 'D', 'E', 'F', 'G'))
#
# for name, member in Group.__members__.items():
#     print(name, member, member.value)

# 自定义
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Tue.value)
for name, member in Weekday.__members__.items():
    print(name, member, member.value)