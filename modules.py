import os
import time
import pandas

while True:
    if os.path.exists('./resources/temps_today.csv'):
        data = pandas.read_csv('./resources/temps_today.csv')
        print(data.mean())
    else:
        print('File does not exist.')
    time.sleep(10)
