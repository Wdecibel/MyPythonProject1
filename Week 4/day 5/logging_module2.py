# __Author__: Han
# __Date__: 2019/1/10

import logging

logger = logging.getLogger()

fh = logging.FileHandler('test.log')    # 创建一个handler，用于写入日志文件
ch = logging.StreamHandler()            # 创建一个handler，用于输出到控制台

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('debug message1')
logger.info('info message2')
logger.warning('warning message3')
logger.error('error message4')
logger.critical('critical message5')

