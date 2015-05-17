# TODO: change column names to appropriate labels

import pandas as pd
import numpy as np
import urllib2
import datetime as dt
import matplotlib.pyplot as plt

def get_google_data(symbol, period, window):
    url_root = 'http://www.google.com/finance/getprices?i='
    url_root += str(period) + '&p=' + str(window)
    url_root += 'd&f=d,o,h,l,c,v&df=cpct&q=' + symbol
    response = urllib2.urlopen(url_root)
    data = response.read().split('\n')

    # the first line contains the full timestamp,
    # every other line is offset from initial timestamp

    parsed_data = []
    anchor_stamp = ''
    for i in range(7, len(data) - 1):
        cdata = data[i].split(',')
        if 'a' in cdata[0]:
            anchor_stamp = cdata[0].replace('a', '')
            cts = int(anchor_stamp)
        else:
            coffset = int(cdata[0])
            cts = int(anchor_stamp) + (coffset * period)

    parsed_data.append((dt.datetime.fromtimestamp(float(cts)), float(cdata[1]),
            float(cdata[2]), float(cdata[3]), float(cdata[4]), float(cdata[5])))

    df = pd.DataFrame(parsed_data)
    df.columns = ['ts','o', 'h', 'l', 'c', 'v']
    df.index = df.ts
    del df['ts']
    return df

def get_spread(base, hedge, ratio, period, window):
    b = get_google_data(base, period, window)
    h = get_google_data(hedge, period, window)
    combo = pd.merge(pd.DataFrame(b.c), pd.DataFrame(h.c), left_index = True,
        right_index = True, how = 'outer')
    combo = combo.fillna(method = 'ffill')
    combo['spread'] = combo.ix[:,0] + ratio * combo.ix[:,1]
    return(combo)

# Download last 10 days of 5 minute data from google finance
spy = get_google_data("SPY", 300, 10)
print spy
# Get the spread between two stocks
spread = get_spread("SSYS", "DDD", -2.0, 60, 15)
print spread