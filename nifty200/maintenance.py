from core.common_maintenance import calculate_time,Maintenance,downloadNIFTYCompaniesList
import os

class HistoryFileNames:
    def __init__(self) -> None:
        self._curFileBaseDir = os.path.split(__file__)[0] + os.path.sep
        self.sixMonthsHistFileName = self._curFileBaseDir + 'nifty200_6_months_history.pkl'
        self.oneYearHistFileName = self._curFileBaseDir + 'nifty200_1y_history.pkl'

class Nifty200:
    def __init__(self) -> None:
        self.fileNames = HistoryFileNames()
        self.symbols = downloadNIFTYCompaniesList(niftyOf=200)
        self.sixMonthMaintenance = Maintenance(
            self.fileNames.sixMonthsHistFileName, self.symbols)
        self.oneYearMaintenance = Maintenance(
            self.fileNames.oneYearHistFileName, self.symbols)

    @calculate_time
    def runMaintenance(self):
        # print("CWD: from nifty200.maintenance:", os.getcwd())
        self._sixMonths()
        self._oneYear()

    def _sixMonths(self):
        self.sixMonthMaintenance.run(months=6)

    def _oneYear(self):
        self.oneYearMaintenance.run(months=12)


if __name__ == '__main__':
    nifty200 = Nifty200()
    nifty200.runMaintenance()
