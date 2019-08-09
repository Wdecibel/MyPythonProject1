#__author__: Han
#date: 2018/11/1

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit(): #长得像不像数字，比如200d，‘200’
    salary = int(salary)
# else:
#     exit('must input digit') #退出程序


print(name, age, job, salary)



msg = '''

-------- info of %s ---------
Name: %s
Age: %d
Job: %s
Salary: %f
You will be retired in %s years
---------- End ----------
'''% (name, name, age, job, salary, 65-age)

print (msg)