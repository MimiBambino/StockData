from google_trends import gtrends
import pandas as pd
import pandas.io.data as web
import datetime as dt
import matplotlib.pyplot as plt


# gt = gtrends(<username>, <password>)

# get weekly search results for FaceBook
vol = gt.get_volume(terms = ["FB"], daily = False)

# convert timestamp into a pandas timestamp
# vol['date'] = 0
# vol.index = [date.split("-")[1] for date in vol.index]
# vol.index = pd.to_datetime(vol.index)

# print vol

# start = dt.datetime(2012, 5, 18)
# end = dt.datetime(2015, 1, 12)

# fb = web.DataReader("FB", 'yahoo', start, end)

# combo = pd.merge(vol, fb[['Close']], left_index = True, right_index = True, how='outer')

# combo = combo.fillna(method='ffill')
# combo = combo.dropna()
# del combo['date']

# combo.plot()

# plt.show()
