# __Author__: Han
# __Date__: 2019/1/10

import logging


# logging.basicConfig(level=logging.DEBUG,    # 设置为最低级别
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log'
#                     )
# Thu, 10 Jan 2019 14:59:46 logging_module.py [line:13] DEBUG debug message
# Thu, 10 Jan 2019 14:59:46 logging_module.py [line:14] INFO info message
# Thu, 10 Jan 2019 14:59:46 logging_module.py [line:15] WARNING warning message
# Thu, 10 Jan 2019 14:59:46 logging_module.py [line:16] ERROR error message
# Thu, 10 Jan 2019 14:59:46 logging_module.py [line:17] CRITICAL critical message

logging.debug('debug message1')
logging.info('info message2')
logging.warning('warning message3')
logging.error('error message4')
logging.critical('critical message5')



