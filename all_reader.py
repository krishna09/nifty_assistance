from nifty50.reader import Nifty50
from nifty100.reader import Nifty100
from nifty200.reader import Nifty200
from core.common_technicals import getBuySignals
n50 = Nifty50()
n100 = Nifty100()
n200 = Nifty200()

#
print("Nifty50 tail\n",n50.sixMonthsData.tail())
print("Nifty100 tail\n",n100.sixMonthsData.tail())
print("Nifty200 tail\n",n200.sixMonthsData.tail())

print(n50.sixMonthsData['TATASTEEL.NS'].columns)

getBuySignals(n50.oneYearData,n50.symbols)
print("")
getBuySignals(n100.oneYearData,n100.symbols)
print("")
getBuySignals(n200.oneYearData,n200.symbols)
