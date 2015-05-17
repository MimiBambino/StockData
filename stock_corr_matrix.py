def stock_corr_matrix(stocks):
    '''
    input a list of stock symbols
    returns a plot showing the correlation against the first stock in the list
    '''

    import pandas.io.data as web
    import datetime as dt
    import numpy as np
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt

    start = dt.datetime(2007, 1, 1)
    end = dt.datetime(2015, 5, 15)

    stuff = []

    for stock in stocks:
        sdata = web.DataReader(stock, 'yahoo', start, end)
        stuff.append(sdata['Close'])

    combo = pd.concat(stuff, axis = 1)
    combo.columns = stocks

    longo = np.log(combo)
    longo = longo.diff().dropna()

    corr = longo.corr()

    sns.set(rc={'figure.facecolor': 'white'})
    ax = sns.heatmap(corr, annot = True, cmap = "PuBu")
    ax.set_title("Stock Correlation Matrix")

    plt.show()

stocks = (['VAW', 'VWO', 'VSS', 'VFH', 'VDE', 'VOX', 'VNQI', 'VXUS','VIS',
        'VCR', 'VDC', 'VHT', 'VGT', 'VNQ', 'VPU'])

stock_corr_matrix(stocks)