import threading
import numpy as np
import requests
from concurrent.futures import ThreadPoolExecutor

from summary.model import Model_YahooFinQuery1

API_URL = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=SYMBOL&region=IN"

def withConcurrentThreadPool(stock_symbols, symbols_per_thread):
    def _getHelperBatchRequest(symbols):
        # print(f"Running with -{threading.currentThread().name} - {len(symbols)}")
        headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"}
        symbol_string = ','.join(symbols)
        symbol_string = symbol_string.replace('&', "%26")
        r = requests.get(API_URL.replace('SYMBOL', symbol_string), headers=headers)
        if r.status_code == 200:
            data = r.json()
            models = Model_YahooFinQuery1.from_dict(data)
            # print(f"Return of -{threading.currentThread().name} - {len(models.quote_response.result)}")
            return models
        else:
            print("Something Wrong with URL get")
            return "Error"

    def _splitter(nifty50_symbols):
        temp = nifty50_symbols
        totalValues = list(set(temp))
        ticker_splits = len(totalValues) // symbols_per_thread
        aa = np.array_split(totalValues, ticker_splits)
        ll = [a.tolist() for a in aa]
        return ll

    symbol_splits = _splitter(stock_symbols)
    finalResults = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(_getHelperBatchRequest, symbol_splits)
        for result in results:
            finalResults.append(result)
    return finalResults


def getCompaniesSummary(symbols):
    # from summary.summary_script import withConcurrentThreadPool
    stocks_models = []
    tempDict = {}
    threadPoolResults = withConcurrentThreadPool(symbols, symbols_per_thread=25)
    for result in threadPoolResults:
        for data in result.quote_response.result:
            if data.regular_market_time is not None:
                stocks_models.append(data)
                tempDict[data.symbol] = data
            else:
                print(f"Stock is not in trading ... NODATA: {data.symbol}")
    return stocks_models, tempDict


def getSymbolsPassedOn6MonthMinCheck(histDF, summaryModelsDict):
    _results = []
    for key, stockModel in summaryModelsDict.items():
        curValue = stockModel.regular_market_price
        _minimum = histDF[key]["Open"][:-1].min()
        _maximum = histDF[key]["Open"][:-1].max()
        # if isCurValueLessThan6MonthMin(stockModel.regular_market_price,histDF[key]):
        if round(curValue, 1) < _minimum:
            _results.append([key, round(_minimum, 2), curValue, round(_maximum, 2),stockModel.short_name])  # min,max in 6 months
    return _results

if __name__ == '__main__':
    from nifty200.reader import Nifty200
    temp_symbols = ['ABB.NS', 'ABBOTINDIA.NS', 'ABCAPITAL.NS', 'ABFRL.NS', 'ACC.NS', 'ADANIENT.NS', 'ADANIGREEN.NS', 'ADANIPORTS.NS', 'ADANITRANS.NS', 'ALKEM.NS', 'AMBUJACEM.NS', 'APOLLOHOSP.NS']
    # results = withConcurrentThreadPool(temp_symbols,5)
    nifty200 = Nifty200()
    # nifty200.getSymbols()
    summaryModels, tempDict = getCompaniesSummary(nifty200.getSymbols())
    output = getSymbolsPassedOn6MonthMinCheck(nifty200.sixMonthsData,tempDict)
    print(len(output))
    # for stock in summaryModels:
    #     print(stock.symbol,stock.regular_market_price)