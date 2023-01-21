import os
from core.common_maintenance import calculate_time,Maintenance,downloadNIFTYCompaniesList


class HistoryFileNames:
    def __init__(self) -> None:
        self._curFileBaseDir = os.path.split(__file__)[0] + os.path.sep
        self.sixMonthsHistFileName = self._curFileBaseDir + 'nifty100_6_months_history.pkl'
        self.oneYearHistFileName = self._curFileBaseDir + 'nifty100_1y_history.pkl'


class Nifty100:
    def __init__(self) -> None:
        self.fileNames = HistoryFileNames()
        self.symbols = downloadNIFTYCompaniesList(niftyOf=100)
        self.sixMonthMaintenance = Maintenance(
            self.fileNames.sixMonthsHistFileName, self.symbols)
        self.oneYearMaintenance = Maintenance(
            self.fileNames.oneYearHistFileName, self.symbols)

    @calculate_time
    def runMaintenance(self):
        # print("CWD: from nifty100.maintenance:", os.getcwd(),"__file__",__file__)
        # print(__file__)
        self._sixMonths()
        self._oneYear()

    def _sixMonths(self):
        self.sixMonthMaintenance.run(months=6)

    def _oneYear(self):
        self.oneYearMaintenance.run(months=12)


if __name__ == '__main__':
    nifty100 = Nifty100()
    nifty100.runMaintenance()
