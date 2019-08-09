# __Author__: Han
# __Date__: 2019/1/25

# 选课系统
# 角色：学校、学院、课程、讲师
# 要求：
# 创建北京、上海2所学校
# 创建linux，python，go 3个课程，linux和python在北京开，go在上海开
# 课程包含，周期，价格，通过学校创建课程
# 通过学校创建班级，班级关联课程、讲师
# 创建讲师角色时要关联学校
# 提供两个角色接口
# 学院视图，可以注册，交学费，选择班级
# 讲师视图，讲师可管理自己的班级，上课时选择班级，查看班级学员列表，修改所管理的学员的成绩
# 管理视图，创建讲师，创建班级，创建课程
# 上面的操作产生的数据都通过pickle序列化保存到文件里


# class Teacher:
#     def __init__(self, name, age, salary=1000):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#
# class Course:
#     def __init__(self, name, teacher, period=1, price=1000):
#         self.name = name
#         self.teacher = teacher
#         self.period = period
#         self.price = price
#
#     def class_up(self):
#
#
# t1 = Teacher('lijie', 8)
# t2 = Teacher('shaobing', 9)
# t3 = Teacher('doubing', 10)
#
# c1 = Course('生理课', t1)
# print(c1.name)
# print(c1.teacher.name)
# print(c1.teacher.age)



























