import requests
import fxcmpy
import socketio



TOKEN = '20acb35862b8cb69aa8fbb4c4e7c98a8a670b827'

con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', server='demo', log_file='log.txt')


instrument = 'BTC/USD'

data = con.get_candles('EUR/USD', period='m1', number=250)

   

print(data)


