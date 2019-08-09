# __Author__: Han
# __Date__: 2019/1/10

import configparser

config = configparser.ConfigParser()

# config['DEFAULT'] = {
#     'ServerAliveInterval': '45',
#     'Compression': 'yes',
#     'Compressionlevel': '9',
#     'ForwardX11': 'yes'
# }
#
# config['bitbucket.org'] = {
#     'User': 'hg'
# }
# config['topsecret.server.com'] = {
#     'Host Port': '50022',
#     'ForwardX11': 'no'
# }
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

# config.read('example.ini')
# print(config.sections())
# print(config.defaults())
# print(config['bitbucket.org']['User'])
# for i in config['bitbucket.org']:
#     print(i)                                # 打印时，DEFAULT都会打印

# config.remove_section('topsecret.server.com')
# print(config.has_section('topsecret.server.com'))

# config.set('bitbucket.org', 'User', 'alex')
# config.remove_option('bitbucket.org', 'User')

# config.write(open('example.ini', 'w'))









