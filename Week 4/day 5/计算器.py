# __Author__: Han
# __Date__: 2019/1/14

# 1.实现加减乘除及括号优先级解析
# 2.用户输入1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))等类似公式后，
# 必须自己解析里面的(),+,-,*,/符号和公式（不能调用eval等类似功能偷懒实现），运算后得出结果，结果必须与真实的计算器所得结果一致

import re

formula_expression = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# input('请输入...')

inner_kuohao = re.findall('\([^()]+\)', formula_expression)
print(inner_kuohao)


def check(target_str):
    flag = True
    if re.findall('[a-zA-Z]', target_str):
        print('Invaild')
        flag = False
    elif re.findall()
    return flag

def formulate(target_str):
    target_str = target_str.replace(' ', '')
    target_str = target_str.replace('++', '+')
    target_str = target_str.replace('+-', '-')
    return target_str


def caculate_multiple(target_str):
    ret = re.search('\d+\.?\d*[*/]\.?\d*', target_str)
        # a,b = re.split('[*/]', ret)
        # a = float(a)
        # b = float(b)
        if
        return
    else:
        pass


def caculate_division(target_str):
    if '/' in target_str:
        tag = target_str.find('/')
        a = tag - 1
        b = tag + 1
        return float(target_str[a]) / float(target_str[b])
    else:
        pass


def caculate_self(target_str):
    if re.search('[$+|$\-)\d]', target_str):




def caculate_plus(target_str):
    if '+' in target_str:



if check(formula_expression):
    formula_expression = formulate(formula_expression)
    while re.search('\(', formula_expression):
        formula_expression = re.search('\([^()]\)', formula_expression).group()


