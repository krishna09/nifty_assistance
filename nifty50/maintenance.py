import os
from core.common_maintenance import calculate_time,Maintenance,downloadNIFTYCompaniesList

class HistoryFileNames:
    def __init__(self) -> None:
        self._curFileBaseDir = os.path.split(__file__)[0] + os.path.sep
        self.sixMonthsHistFileName = self._curFileBaseDir + 'nifty50_6_months_history.pkl'
        self.oneYearHistFileName = self._curFileBaseDir + 'nifty50_1y_history.pkl'


class Nifty50:
    def __init__(self) -> None:
        self.fileNames = HistoryFileNames()
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

    
    
    