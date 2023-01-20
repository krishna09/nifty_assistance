import os
import time
from datetime import datetime
import pandas as pd
import yfinance as yf


def calculate_time(func):
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        output = func(*args, **kwargs)
        # storing time after function execution
        end = time.time()
        print(
            f"Total time taken for {func.__name__} : {round(end - begin,3)} sec"
        )
        return output

    return inner1


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


def saveHistoryAsPickle(multiIdx_df, filenName):
    # with open(filenName, 'w') as fp:
    multiIdx_df.to_pickle(filenName)
    print("history data stored")


@calculate_time
def readHistoryFromPickle(fileName):
    try:
        df = pd.read_pickle(fileName)
        return df
    except Exception as error:
        print(f"Error During Pickle file : {fileName} reading, Error: {error}")
        return None


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
                self.invokeOneDay_OHLC_Downloader()
                self.append_1D_OHLC_To_HistoryFile()

    def invokeSixMonthsDownloader(self,offset):
        print("Running invokeSixMonthsDownloader")
        startDate = datetime.today() - pd.offsets.DateOffset(months=offset)
        startDate = startDate.strftime("%Y-%m-%d")
        endDate = datetime.today().strftime("%Y-%m-%d")
        print(f"Current dates: start:{startDate},end:{endDate}")
        self.historyDF = downloadHistory(self.symbols, startDate, endDate)
        saveHistoryAsPickle(self.historyDF, self.filename)

    def invokeOneDay_OHLC_Downloader(self):
        print("Running invokeOneDay_OHLC_Downloader")
        self.todaysOHLC_DF = get_1day_OHLC(self.symbols)

    def append_1D_OHLC_To_HistoryFile(self):
        curHistoryDF = readHistoryFromPickle(self.filename)
        tempDF = pd.concat([curHistoryDF, self.todaysOHLC_DF])
        saveHistoryAsPickle(tempDF, self.filename)

@calculate_time
def downloadNIFTYCompaniesList(niftyOf):
    nifty_url = f"https://www1.nseindia.com/content/indices/ind_nifty{niftyOf}list.csv"
    df = pd.read_csv(nifty_url)
    mylist = df["Symbol"].tolist()
    nifty_list = [val + ".NS" for val in mylist]
    return nifty_list


class NIFTY50_HistoryFileNames:
    def __init__(self) -> None:
        self._curFileBaseDir = os.path.split(__file__)[0] + os.path.sep
        self.sixMonthsHistFileName = self._curFileBaseDir + 'nifty50_6_months_history.pkl'
        self.oneYearHistFileName = self._curFileBaseDir + 'nifty50_1y_history.pkl'

class Nifty50:
    def __init__(self) -> None:
        self.fileNames = NIFTY50_HistoryFileNames()
        self.symbols = downloadNIFTYCompaniesList(niftyOf=50)
        self.sixMonthMaintenance = Maintenance(
            self.fileNames.sixMonthsHistFileName,self.symbols)
        self.oneYearMaintenance = Maintenance(
            self.fileNames.oneYearHistFileName,self.symbols)
    @calculate_time
    def runMaintenance(self):
        # print("CWD: from nifty50.maintenance:",os.getcwd())
        self._sixMonths()
        self._oneYear()

    def _sixMonths(self):
        self.sixMonthMaintenance.run(months=6)

    def _oneYear(self):
        self.oneYearMaintenance.run(months=12)
    
if __name__ == '__main__':
    nifty50 = Nifty50()
    nifty50.runMaintenance()
    # nifty50.sixMonthMaintenance.invokeOneDay_OHLC_Downloader()
    # print(nifty50.sixMonthMaintenance.todaysOHLC_DF.tail())

    
    
    