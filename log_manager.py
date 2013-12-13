import logging
import sys

hide_logger = logging.getLogger('file_hider.HIDE')
unhide_logger = logging.getLogger('file_hider.UNHIDE')
# create logger with 'spam_application'
logger = logging.getLogger('file_hider')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('file_hider.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

def log_hide(file):
    hide_logger.info(file)

def log_unhide(file):
    unhide_logger.info(file)
'''
print sys.argv[0]
if (sys.argv[0]=='HIDE'):
    log_hide(sys.argv[1])
elif (sys.argv[0]=='UNHIDE'):
    log_unhide(sys.argv[1])
'''