def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import time
import logging
import absl.logging
logging.root.removeHandler(absl.logging._absl_handler)
absl.logging._warn_preinit_stderr = False
logging.basicConfig(filename='log.txt', filemode='w', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO, format='%(asctime)-15s %(message)s')
logging.info('logs to file, as expected')
from iqoptionapi.stable_api import IQ_Option

API = IQ_Option("rashedhasanai@gmail.com","rostugbot007")
API.connect()
API.change_balance('PRACTICE') # PRACTICE / REAL
while True:
    if API.check_connect() == False:
        print('Erro ao se conectar')
        API.connect()
    else:
    	print('Conectado com sucesso')
    	break
while True:
    i1=API.get_candles("EURUSD",120,1,time.time())
    print(i1)
