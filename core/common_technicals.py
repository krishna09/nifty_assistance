import numpy as np
import pandas as pd
pd.set_option('mode.chained_assignment', None)
import ta
## BUY = MACD line above signal line indicates good time to BUY
## IF MACD LINE > SIGNAL LINE => BUY THE STOCK
## IF SIGNAL LINE > MACD LINE => SELL THE STOCK

"""
The moving average convergence/divergence (MACD, or MAC-D) line is calculated by subtracting the 26-period exponential 
moving average (EMA) from the 12-period EMA. The signal line is a nine-period EMA of the MACD line. MACD is best used 
with daily periods, where the traditional settings of 26/12/9 days is the norm
"""

def get_Technical_Decision_Lines(symbols,mulIdx_df):
    for symbol in symbols:
        _temp_df = MACD_Decision(mulIdx_df[symbol])
        mulIdx_df[symbol, 'MACD_Diff'] = _temp_df['MACD_Diff']
        mulIdx_df[symbol, 'MACD_Decision'] = _temp_df['MACD_Decision']
        _temp_df = GoldenCrossDecision(mulIdx_df[symbol])
        mulIdx_df[symbol,'SMA20'] = _temp_df['SMA20']
        mulIdx_df[symbol,'SMA50'] = _temp_df['SMA50']
        mulIdx_df[symbol,'GC_Signal'] = _temp_df['GC_Signal']
        mulIdx_df[symbol,'GC_Decision'] = _temp_df['GC_Decision']
        _temp_df = RSI_SMA_Decision(mulIdx_df[symbol])
        mulIdx_df[symbol,'RSI'] = _temp_df['RSI']
        mulIdx_df[symbol,'SMA200'] = _temp_df['SMA200']
        mulIdx_df[symbol,'RSI_Decision'] = _temp_df['RSI_Decision']
    return mulIdx_df
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

def MACD_Decision(df:pd.DataFrame):
    _temp_df = pd.DataFrame()
    _temp_df['MACD_Diff'] = ta.trend.macd_diff(df.Close)
    _temp_df['MACD_Decision'] = np.where((_temp_df.MACD_Diff > 0) & (_temp_df.MACD_Diff.shift(1) < 0),True,False)
    return _temp_df
def GoldenCrossDecision(df:pd.DataFrame):
    _temp_df = pd.DataFrame()
    _temp_df['SMA20'] = ta.trend.sma_indicator(df.Close,window=20)
    _temp_df['SMA50'] = ta.trend.sma_indicator(df.Close, window=50)
    _temp_df['GC_Signal'] = np.where(_temp_df.SMA20 > _temp_df.SMA50,True,False)
    _temp_df['GC_Decision'] = _temp_df.GC_Signal.diff()
    return _temp_df

def RSI_SMA_Decision(df:pd.DataFrame):
    _temp_df = pd.DataFrame()
    _temp_df['RSI'] = ta.momentum.rsi(df.Close,window=10)
    _temp_df['SMA200'] = ta.trend.sma_indicator(df.Close,window=200)
    _temp_df['RSI_Decision'] = np.where((df.Close > _temp_df.SMA200) & (_temp_df.RSI < 30),True,False)
    return _temp_df

def applyTechnicals(df:pd.DataFrame):
    df = MACD_Decision(df)
    df = GoldenCrossDecision(df)
    df = RSI_SMA_Decision(df)
    return df

def getBuySignals(multiIdxDF:pd.DataFrame,symbols:list):
    indicators = ['MACD_Decision', 'GC_Decision', 'RSI_Decision']
    for symbol in symbols:
        if multiIdxDF[symbol].empty is False:
            for indicator in indicators:
                if multiIdxDF[symbol, indicator].iloc[-1]:
                    print(f"{indicator} Buying Signal for {symbol}")

if __name__ == '__main__':
    from nifty50.reader import Nifty50

    n50 = Nifty50()
    # print(GoldenCrossDecision(n50.sixMonthsData['TATASTEEL.NS']))
    # _finalDF = n50.sixMonthsData['TATASTEEL.NS']
    # print(n50.sixMonthsData['INDUSINDBK.NS'].columns)
    n50.sixMonthsData = get_Technical_Decision_Lines(n50.symbols,n50.sixMonthsData)
    getBuySignals(n50.sixMonthsData,n50.symbols)
    # print(n50.sixMonthsData['INDUSINDBK.NS'].columns)
    # indicators = ['MACD_Decision','GC_Decision','RSI_Decision']
    # for symbol in n50.symbols:
    #     if n50.sixMonthsData[symbol].empty is False:
    #         for indicator in indicators:
    #             if n50.sixMonthsData[symbol, indicator].iloc[-1]:
    #                 print(f"{indicator} Buying Signal for {symbol}")