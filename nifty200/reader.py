from core.common_maintenance import readHistoryFromPickle
from core.common_technicals import get_Technical_Decision_Lines
from nifty200.maintenance import HistoryFileNames

class Nifty200:
    def __init__(self):
        self.fileNames = HistoryFileNames()
        self.sixMonthsData = readHistoryFromPickle(self.fileNames.sixMonthsHistFileName)
        self.oneYearData = readHistoryFromPickle(self.fileNames.oneYearHistFileName)
        self.symbols = self.getSymbols()
        self.figOneYear = None
        self.figSixMonths = None
        # self.sixMonthsData = get_Technical_Decision_Lines(self.symbols, self.sixMonthsData)
        # self.oneYearData = get_Technical_Decision_Lines(self.symbols, self.oneYearData)

    def getSymbols(self):
        return list(self.sixMonthsData.columns.levels[0])

    def getDataBetweenDates(self,startDate,endDate):
        pass

    def viewData(self,showFig=False):
        self.figSixMonths = self._showData(self.sixMonthsData, title="6",showFig=showFig)
        self.figOneYear = self._showData(self.oneYearData, title="12",showFig=showFig)

    def getLastDayData(self,months):
        if months == 6:
            return self.sixMonthsData[self.sixMonthsData.index[-1]]
        else:
            return self.oneYearData[-1]

    @staticmethod
    def _showData(df, title,showFig):
        # df = self.sixMonthsData
        from plotly.subplots import make_subplots
        import plotly.graph_objs as go
        # plotly setup
        plot_cols = 4
        plot_rows = len(df.columns.levels[0]) // plot_cols
        plot_subTitles = [f"{idx + 1}_{col}" for idx, col in enumerate(df.columns.levels[0])]
        fig = make_subplots(rows=plot_rows, cols=plot_cols, subplot_titles=plot_subTitles, )

        # add traces
        x = 0
        for i in range(1, plot_rows + 1):
            for j in range(1, plot_cols + 1):
                # print(str(i)+ ', ' + str(j))
                fig.add_trace(go.Scatter(x=df.index, y=df[df.columns.levels[0][x]]["Open"].values, mode='lines'),
                              # name=df.columns.levels[0][x],),
                              row=i, col=j)
                fig.add_trace(
                    go.Scatter(x=df.index, y=df[df.columns.levels[0][x]]["Open"].rolling(5).mean(), mode='lines',
                               name="MA5"),
                    # name=df.columns.levels[0][x],),
                    row=i, col=j)
                x = x + 1
        # Format and show fig
        fig.update_layout(title=f"NIFTY 200 {title} Month History Data", showlegend=False)
        # fig.update_layout(height=1200 * 8, width=1400)
        fig.update_layout(height=1200 * 8, width=1500)
        if showFig:
            fig.show()
        return fig
        # fig.write_image("something.png")
        # fig.write_image("something.png")



if __name__ == '__main__':
    nifty200 = Nifty200()
    print(nifty200.sixMonthsData.tail())
    # nifty200.viewData()
    # df = nifty200.getLastDayData(months=6)
    # print(df)