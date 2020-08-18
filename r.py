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
import investpy
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
      

def news(news_name):
  s=investpy.get_calendar('GMT +6:00','time_only',None,['high'],None,None,None)
  i=0
  while True:
    if s['event'][i]==news_name:
      break
    else:
      i=i+1
  return i
print(news('Retail Sales (MoM)  (Jul)'))

def buyoption(forecast,actual):
  if forecast[0]<=actual[0]:
    status,id = API.buy(200,"USDJPY",'call',1)
    print("buy")
  elif forecast[0]>=actual[0]:
    status,id = API.buy(200,"USDJPY",'put',1)
    print("sell")
  else:
    None
while True:
  s=investpy.get_calendar('GMT +6:00','time_only',None,['high'],None,None,None)
  j=news('Building Permits  (Jul)')
  fore=s['forecast'][j]
  act=s['actual'][j]
  if fore!=None and act!=None:
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in fore)
    forecast= [float(i) for i in newstr.split()]
    print(forecast)
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in act)
    actual= [float(i) for i in newstr.split()]
    print(actual)
    buyoption(forecast,actual)
    break
  else:
    None
