# __Author__: Han
# __Date__: 2019/1/15

# 1.实现加减乘除及括号优先级解析
# 2.用户输入1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))等类似公式后，
# 必须自己解析里面的(),+,-,*,/符号和公式（不能调用eval等类似功能偷懒实现），运算后得出结果，结果必须与真实的计算器所得结果一致
import re


# 输入合法性检验
def check(target_str):
    flag = True
    if re.findall('[a-zA-Z]', target_str):
        print('Contain Alphabets')
        flag = False
    else:
        pass
    return flag


# 重复性符号检验
def formulate(target_str):
    target_str = target_str.replace(' ', '')
    target_str = target_str.replace('++', '+')
    target_str = target_str.replace('+-', '-')
    target_str = target_str.replace('--', '+')
    target_str = target_str.replace('*+', '*')
    target_str = target_str.replace('/+', '/')
    return target_str


# 正式计算
formula_expression = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

if check(formula_expression):
    formula_expression = formulate(formula_expression)
    while True:
        if '(' in formula_expression:
            formula_expression = re.search('\([^()]+\)', formula_expression)


ret = re.search('\d+\.?\d*[*/]\.?\d*', formula_expression)

print(ret.group())








