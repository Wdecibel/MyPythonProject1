# __Author__: Han
# __Date__: 2019/1/11

# Q：正则表达式是用来干什么的？A：匹配字符串

# s = 'hello world'

# print(s.find('ll'))
# ret = s.replace('ll', 'xx')
# print(ret)
# print(s.split(' '))

# str提供的方法是完全匹配，无法提供模糊匹配
# 引入正则表达式：模糊匹配

import re

# ret = re.findall('w\w{2}l', 'hellow world  wdfl')
# print(ret)

# print('sdfoaindifofnalexljoiwniof'.find('alex'))

# 元字符('.', '^', '$', '*', '+', '?', '{}', '[]', '|', '()', '\')

# '.'：通配符
# ret = re.findall('w..l', 'hello world')  # 可代指所有的字符（除换行符\n），且仅可代指一位
# print(ret)

# ret = re.findall('w..l', 'hello w\t ld')  # 除非改第三个参数
# print(ret)

# '^'：开头
# ret = re.findall('^h...o', 'hasdoadifjnisadfhello')    # 仅从开头匹配
# print(ret)

# '$'：结尾
# ret = re.findall('a..x$', 'asdfasdgalexruioinalex')
# print(ret)

# '*'：重复之前的匹配{0,}
# ret = re.findall('ab*', 'asdfawefasaaabaaaadfewafalexliwefwefwefawefwefewfweflia')
# print(ret)

# '+'：{1,}
# ret = re.findall('ab+', 'kjoijija')
# print(ret)

# ret = re.findall('a+b', 'aaaabboijoib')
# print(ret)

# '?'：{0, 1}
# ret = re.findall('a?b', 'aaaabboijoib')
# print(ret)

# '{}'：自定义范围匹配, 什么都不加代表无穷
# ret = re.findall('a{1,3}b', 'aaaaabbbbaaaaaaaaaaaaaaaab')   # 贪婪匹配，按最多的匹配
# print(ret)

# '[]'：字符集, 或的关系，且必须为一个字符；
# ret = re.findall('[a-z]', 'adx')
# print(ret)

# '[]'：也可取消元字符的特殊功能(\ ^ -)
# ret = re.findall('[w,]', 'adwdx,')
# print(ret)

# ret = re.findall('[1-9a-zA-Z]', '12tyAS,')
# print(ret)

# '^'：放在[]里：取反
# ret = re.findall('[^4,5]', 'iu12t4yA5S,')   # 逗号也包含在内
# print(ret)

# '\'：后跟元字符去除特殊功能；后跟普通字符实现特殊功能（）
# \d：匹配任何十进制数[0-9]
# \D：匹配任何非数字字符[^0-9]
# \s：匹配任何空白字符[\t\n\r\f\v]
# \S：匹配任何非空白字符[^\t\n\r\f\v]
# \w：匹配任何字母数字字符[a-zA-Z0-9_]
# \W：匹配任何非字母数字字符[^a-zA-Z0-9_]
# \b：匹配一个特殊字符边界，也就是指单词和空格间的位置
# ret = re.findall('\w', 'asdf89\r\n18\t91  saSD_FAdfds1\ndf186')
# print(ret)

# ret = re.findall(r'I\b', 'hello, I am a LI$T')
# print(ret)

# 匹配出第一个满足条件的结果
# ret = re.search('sb', 'dfajldskjsbslkdjflsb')
# print(ret)  # <_sre.SRE_Match object; span=(9, 11), match='sb'>
# print(ret.group())

# ret = re.search('a\.', 'a.jsdif').group()
# print(ret)

# ret = re.search('a\+', 'a+gj').group()
# print(ret)

# ret = re.findall(r'\\', 'abdadsf\ppasdf')
# print(ret)

# m = re.search(r'\bblow', 'blow')
# print(m)

# () |

# m = re.search('(as)+', 'asasdiofjioasdbv')
# print(m.group())

# m = re.search('(as)|3', '3asasdiofjio3asdbv')
# print(m.group())

# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})', 'weeew34ttt123/ooo')
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))

# 正则表达式的方法
# 1.findall(): 所有结果都返回到一个列表里面
# 2.search(): 返回匹配到的一个对象(object)，课可以调用group()获取返回结果
# 3.match(): 只在字符串开始匹配，也返回匹配到的第一个对象
# 4.split():

# ret = re.match('asd', 'asddfasd')
# print(ret.group())

# print('asdf'.split('s'))
# ret = re.split('[ka]', 'djk,sal')
# print(ret)

# ret = re.split('[ks]', 'sa;ijifkafslj')  # ['', 'a;ijif', 'af', 'lj']
# print(ret)

# ret = re.sub('a..x', 's..b', 'hluiosjoifalexasidnf')    # str.replace()
# print(ret)

# ret = re.sub('a..x', 's..b', 'hluiosjoifalexasidnf')
# print(ret)

# ret = re.findall('\.com', 'https://www.bilibili.com/video/av13690129/?p=126')
# ret = re.findall('\.com', 'https://www.bilibili.com/video/av13690129/?p=126')

# obj = re.compile('\.com')
# print(obj.findall('https://www.bilibili.com/video/av13690129/?p=126'))


# print(re.search('[$+|$\-)]\d+', 'bili1165').group())


