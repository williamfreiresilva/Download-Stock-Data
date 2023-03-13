import requests
import time
from datetime import datetime

ticker = input('Enter the ticker symbol: ')
from_date = input('Enter start date in yyyy/mm/dd format: ')
to_date = input('Enter end date in yyyy/mm/dd format: ')

def convert_time(date):
  d = datetime.strptime(date, '%Y/%m/%d')
  epoch = time.mktime(d.timetuple())
  return int(epoch)

from_date = convert_time(from_date)
to_date = convert_time(to_date)

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_date}&period2={to_date}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content

with open('data.csv','wb') as file:
  file.write(content)