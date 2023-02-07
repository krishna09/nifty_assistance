from summary.summaryWithThreadPool import getCompaniesSummary,getSymbolsPassedOn6MonthMinCheck
from nifty50.reader import Nifty50
from nifty100.reader import Nifty100
from nifty200.reader import Nifty200

def _makeGreenText(rowData):
    _temp = []
    for val in rowData:
        _temp.append("[green]" + str(val) + "[/]")
    return _temp

def coloredTable(stocks_data ,title=""):
    from rich.console import Console
    from rich.table import Table

    console = Console(width=150)

    table = Table(show_header=True, header_style="bold magenta")
    table.title = "NIFTY Companies last one year min value check"
    table.add_column("Symbol",justify="left",style="white")
    table.add_column("MinVal",justify="left",style="white")
    table.add_column("CurVal", justify="left",style="white") #grey93
    table.add_column("MaxVal", justify="left", style="white")
    table.add_column("Short Name", justify="left", style="white",no_wrap=True)
    table.add_column("NIFTY-50",justify="left",style="white")
    table.add_column("NIFTY-100", justify="left", style="white")
    table.add_column("NIFTY-200", justify="left", style="white")
    symbols_n50 = n50.getSymbols()
    symbols_n100 = n100.getSymbols()
    symbols_n200 = n200.getSymbols()
    stocks_data.sort(key=lambda x:x[0])
    for data in stocks_data:
        c1,c2,c3,c4,c5 = data
        c6 = str('YES') if c1 in symbols_n50 else str('NO')
        c7 = str('YES') if c1 in symbols_n100 else str('NO')
        c8 = str('YES') if c1 in symbols_n200 else str('NO')
        if c6 == 'YES' or c7=='YES':
            table.add_row(*_makeGreenText([c1,c2,c3,c4,c5,c6,c7,c8]))
        else:
            table.add_row("[white]"+c1+"[/]",str(c2),str(c3),str(c4),c5,c6,c7,c8)

    # table.min_width = None
    console.print(table)

def printInTableFormat(stocks_data,title):
#https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
    from prettytable import PrettyTable
    table = PrettyTable(['Symbol', 'MinValue','CurValue','MaxValue','Short Name'])
    table.title = title
    for stock in stocks_data:
        table.add_row(stock)
    table[0].align = "l"
    # table.set_cols_align(['l', 'l', 'r', 'r'])
    print(table)

n50 = Nifty50()
n100 = Nifty100()
n200 = Nifty200()

summaryModels, tempDict = getCompaniesSummary(n200.getSymbols())
output = getSymbolsPassedOn6MonthMinCheck(n200.oneYearData,tempDict)
coloredTable(output)