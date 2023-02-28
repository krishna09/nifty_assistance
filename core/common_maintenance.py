import os
import time
from datetime import datetime
import pandas as pd
import yfinance as yf
from core.common_technicals import get_Technical_Decision_Lines
def calculate_time(func):
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        output = func(*args, **kwargs)
        # storing time after function execution
        end = time.time()
        print(f"Total time taken for {func.__name__} : {round(end - begin,3)} sec")
        return output
    return inner1

# @calculate_time
def downloadNIFTYCompaniesList(niftyOf):
    nifty_url = f"https://www1.nseindia.com/content/indices/ind_nifty{niftyOf}list.csv"
    df = pd.read_csv(nifty_url)
    mylist = df["Symbol"].tolist()
    nifty_list = [val + ".NS" for val in mylist]
    return nifty_list


@calculate_time
def downloadHistory(symbols, startDate, endDate):
    history_data = yf.download(symbols,
                               group_by='ticker',
                               start=startDate,
                               end=endDate,
                               threads=True,
                               progress=False)
    return history_data


@calculate_time
def get_1day_OHLC(symbols):
    oneDayData = yf.download(symbols,
                             period='1d',
                             group_by='ticker',
                             threads=True,
                             progress=False)
    return oneDayData


def saveHistoryAsPickle(multiIdx_df, fileName):
    # with open(fileName, 'w') as fp:
    multiIdx_df.to_pickle(fileName)
    print("history data stored")


# @calculate_time
def readHistoryFromPickle(fileName):
    try:
        df = pd.read_pickle(fileName)
        return df
    except Exception as error:
        print(f"Error During Pickle file : {fileName} reading, Error: {error}")
        return None


# class NIFTY_HistoryFileNames:
#     def __init__(self,niftyOf) -> None:
#         print(f"CWD:{os.getcwd()}")
#         print(f"__FILE__:{__file__}")
#         # self._curFileBaseDir = os.path.split(__file__)[0] + os.path.sep
#         self._curFileBaseDir = os.getcwd() + os.path.sep + f"nifty{niftyOf}" + os.path.sep
#         print(f"self._curFileBaseDir:{self._curFileBaseDir}")
#         self.sixMonthsHistFileName = self._curFileBaseDir + f'nifty{niftyOf}_6_months_history.pkl'
#         self.oneYearHistFileName = self._curFileBaseDir + f'nifty{niftyOf}_1y_history.pkl'

# class NIFTY100_HistoryFileNames:
#     def __init__(self) -> None:
#         self._curFileBaseDir = os.path.split(__file__)[0] + os.path.sep
#         self.sixMonthsHistFileName = self._curFileBaseDir + 'nifty100_6_months_history.pkl'
#         self.oneYearHistFileName = self._curFileBaseDir + 'nifty100_1y_history.pkl'
#
# class NIFTY200_HistoryFileNames:
#     def __init__(self) -> None:
#         self._curFileBaseDir = os.path.split(__file__)[0] + os.path.sep
#         self.sixMonthsHistFileName = self._curFileBaseDir + 'nifty200_6_months_history.pkl'
#         self.oneYearHistFileName = self._curFileBaseDir + 'nifty200_1y_history.pkl'
#


class Maintenance:
    def __init__(self, filename, symbols) -> None:
        self.filename = filename
        self.symbols = symbols
        self.historyDF = None
        self.todaysOHLC_DF = None

    def run(self,months):
        if not os.path.exists(self.filename):
            self.invokeSixMonthsDownloader(months)
        else:
            _curHistoryDF = readHistoryFromPickle(self.filename) # to eliminate unnecessary download call
            print(f"History last entry day:{_curHistoryDF.index[-1].day},curDay:{datetime.today().day}")
            if _curHistoryDF.index[-1].day == datetime.today().day:
                print(f'Todays:{datetime.today().strftime("%Y-%m-%d")} Data Already Present in the File')
                return
            else:
                # to avoid full symbols access when not required
                _tempDF = get_1day_OHLC(self.symbols[:2])
                if _tempDF.index[-1] ==_curHistoryDF.index[-1]:
                    print(f"History File Already contains last traded day data: Last Entry{_curHistoryDF.index[-1]}")
                    return
                if (_tempDF.index[-1] - _curHistoryDF.index[-1]).days >=2:
                    self.invokeSixMonthsDownloader(offset=months) #TODO: here it can be optimized
                    return
                self.invokeOneDay_OHLC_Downloader()
                self.append_1D_OHLC_To_HistoryFile()
                #reapply technicals on new data appended


    def invokeSixMonthsDownloader(self,offset):
        print("Running invokeSixMonthsDownloader")
        startDate = datetime.today() - pd.offsets.DateOffset(months=offset)
        startDate = startDate.strftime("%Y-%m-%d")
        endDate = datetime.today().strftime("%Y-%m-%d")
        print(f"Current dates: start:{startDate},end:{endDate}")
        self.historyDF = downloadHistory(self.symbols, startDate, endDate)
        self.historyDF = get_Technical_Decision_Lines(self.symbols,self.historyDF)
        saveHistoryAsPickle(self.historyDF, self.filename)

    def invokeOneDay_OHLC_Downloader(self):
        print("Running invokeOneDay_OHLC_Downloader")
        self.todaysOHLC_DF = get_1day_OHLC(self.symbols)

    def append_1D_OHLC_To_HistoryFile(self):
        curHistoryDF = readHistoryFromPickle(self.filename)
        tempDF = pd.concat([curHistoryDF, self.todaysOHLC_DF])
        tempDF = get_Technical_Decision_Lines(self.symbols,tempDF) # TODO: is it right place?
        saveHistoryAsPickle(tempDF, self.filename)

if __name__ == '__main__':
    pass
    # nn = NIFTY_HistoryFileNames(niftyOf=50)
    # print(nn.oneYearHistFileName)