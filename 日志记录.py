import logging
logging.basicConfig(filename='f:\\mylog1.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')

print(1/0)
logging.info('除法成功')
logging.info('ending program')
