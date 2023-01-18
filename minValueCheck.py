from summary.summaryWithThreadPool import getCompaniesSummary,getSymbolsPassedOn6MonthMinCheck
from nifty50.reader import Nifty50
from nifty100.reader import Nifty100
from nifty200.reader import Nifty200

# n50 = Nifty50()
# n100 = Nifty100()
n200 = Nifty200()
print("6-Months")
# print(f"\t************** NIFTY-50 **************")
# summaryModels, tempDict = getCompaniesSummary(n50.getSymbols())
# output = getSymbolsPassedOn6MonthMinCheck(n50.sixMonthsData,tempDict)
# print("\tTotal Symbols:",len(output))
# print(f"\t{output}")
#
# print(f"\t************** NIFTY-100 **************")
# summaryModels, tempDict = getCompaniesSummary(n100.getSymbols())
# output = getSymbolsPassedOn6MonthMinCheck(n100.sixMonthsData,tempDict)
# print("\tTotal Symbols:",len(output))
# print(f"\t{output}")

print(f"\t************** NIFTY-200 **************")
summaryModels, tempDict = getCompaniesSummary(n200.getSymbols())
output = getSymbolsPassedOn6MonthMinCheck(n200.sixMonthsData,tempDict)
print("\tTotal Symbols:",len(output))
print(f"\t{output}")


print("1-Year")
# print(f"\t************** NIFTY-50 **************")
# summaryModels, tempDict = getCompaniesSummary(n50.getSymbols())
# output = getSymbolsPassedOn6MonthMinCheck(n50.oneYearData,tempDict)
# print("\tTotal Symbols:",len(output))
# print(f"\t{output}")
#
# print(f"\t************** NIFTY-100 **************")
# summaryModels, tempDict = getCompaniesSummary(n100.getSymbols())
# output = getSymbolsPassedOn6MonthMinCheck(n100.oneYearData,tempDict)
# print("\tTotal Symbols:",len(output))
# print(f"\t{output}")

print(f"\t************** NIFTY-200 **************")
summaryModels, tempDict = getCompaniesSummary(n200.getSymbols())
output = getSymbolsPassedOn6MonthMinCheck(n200.oneYearData,tempDict)
print("\tTotal Symbols:",len(output))
print(f"\t{output}")
