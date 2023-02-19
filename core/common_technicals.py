import numpy as np

## BUY = MACD line above signal line indicates good time to BUY
## IF MACD LINE > SIGNAL LINE => BUY THE STOCK
## IF SIGNAL LINE > MACD LINE => SELL THE STOCK

"""
The moving average convergence/divergence (MACD, or MAC-D) line is calculated by subtracting the 26-period exponential 
moving average (EMA) from the 12-period EMA. The signal line is a nine-period EMA of the MACD line. MACD is best used 
with daily periods, where the traditional settings of 26/12/9 days is the norm
"""

def find_MACD_Signal_Lines(symbols, mulIdx_df):
    for symbol in symbols:
        shortEMA = mulIdx_df[symbol].Close.ewm(span=12, adjust=False).mean()
        # long EMA = Exponential Moving Average
        longEMA = mulIdx_df[symbol].Close.ewm(span=26, adjust=False).mean()
        # calculate MAC-D line
        # MACD = shortEMA - longEMA
        MACD = longEMA - shortEMA # TODO: Cross Verify the logic
        # calculate signal line
        signal = MACD.ewm(span=9, adjust=False).mean()
        mulIdx_df[symbol, 'MACD'] = MACD
        mulIdx_df[symbol, 'Signal'] = signal
        b_s = get_Buy_Sell_Signals(mulIdx_df[symbol])
        mulIdx_df[symbol,'Buy_Signal_Price'] = b_s[0]
        mulIdx_df[symbol,'Sell_Signal_Price'] = b_s[1]
    return mulIdx_df

def get_Buy_Sell_Signals(signal): # TODO: Cross Verify the logic
    buy = []
    sell = []
    flag = -1
    for i in range(0,len(signal)):
        if signal['MACD'][i] > signal['Signal'][i]:
            sell.append(np.nan)
            if flag != 1:
                buy.append(signal['Close'][i])
                flag = 1
            else:
                buy.append(np.nan)

        elif signal['MACD'][i] < signal['Signal'][i]:
            buy.append(np.nan)
            if flag != 0:
                sell.append(signal['Close'][i])
                flag = 0
            else:
                sell.append(np.nan)
        else:
            buy.append(np.nan)
            sell.append(np.nan)
    return buy,sell
