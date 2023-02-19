from nifty50.reader import Nifty50
import matplotlib.pyplot as plt
# plt.style.use('fivethirtyeight')
# import pandas as pd
# # pd.set_option('mode.chained_assignment', 'raise')
# pd.set_option('mode.chained_assignment', None) # to ignore all warnings but make sure what you are doing

n50  = Nifty50()

df = n50.oneYearData['TATASTEEL.NS']

plt.figure('MACD Signal',figsize=(13,7))
plt.plot(df.index,df['MACD'],label='TATASTEEL.NS MACD',color='red')
plt.plot(df.index,df['Signal'],label='signal line',color='blue')
plt.legend(loc='upper left')

plt.figure('BUY/SELL Signals',figsize=(13,7))
plt.scatter(df.index,df['Buy_Signal_Price'],color='r',label='Buy',marker='^',alpha=1)
plt.scatter(df.index,df['Sell_Signal_Price'],color='g',label='Sell',marker='v',alpha=1)
plt.plot(df['Close'],label='Close Price',alpha=0.35)
plt.title('Close Price Buy/Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(loc='upper left')

plt.show()



# plt.figure('data',figsize=(13,7))
# plt.plot(df['Close'],label='Close')
# plt.title('TATASTEEL.NS Close Price History')
# plt.xlabel('Date')
# plt.ylabel('Price in Rupees \u20B9')

## BUY = MACD line above signal line indicates good time to BUY
## IF MACD LINE > SIGNAL LINE => BUY THE STOCK
## IF SIGNAL LINE > MACD LINE => SELL THE STOCK

#calculate MACD
"""
The moving average convergence/divergence (MACD, or MAC-D) line is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA. The signal line is a nine-period EMA of the MACD line. MACD is best used with daily periods, where the traditional settings of 26/12/9 days is the norm
"""
# #short EMA = exponential Moving Average
# shortEMA = df.Close.ewm(span=12,adjust=False).mean()
# #long EMA = Exponential Moving Average
# longEMA = df.Close.ewm(span=26,adjust=False).mean()
# #calculate MAC-D line
# # MACD = shortEMA - longEMA
# MACD =  longEMA - shortEMA
# #calculate signal line
# signal = MACD.ewm(span=9,adjust=False).mean()
#
# df['MACD'] = MACD
# df['Signal'] = signal


#
# def buy_sell(signal):
#     buy = []
#     sell = []
#     flag = -1
#     for i in range(0,len(signal)):
#         if signal['MACD'][i] > signal['Signal'][i]:
#             sell.append(np.nan)
#             if flag != 1:
#                 buy.append(signal['Close'][i])
#                 flag = 1
#             else:
#                 buy.append(np.nan)
#
#         elif signal['MACD'][i] < signal['Signal'][i]:
#             buy.append(np.nan)
#             if flag != 0:
#                 sell.append(signal['Close'][i])
#                 flag = 0
#             else:
#                 sell.append(np.nan)
#         else:
#             buy.append(np.nan)
#             sell.append(np.nan)
#     return buy,sell
#
# b_s = buy_sell(df)
#
# df['Buy_Signal_Price'] = b_s[0]
# df['Sell_Signal_Price'] = b_s[1]


