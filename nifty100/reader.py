# from nifty100 import maintenance
from nifty100.maintenance import NIFTY100_HistoryFileNames,readHistoryFromPickle
class Nifty100:
    def __init__(self):
        self.fileNames = NIFTY100_HistoryFileNames()
        self.sixMonthsData = readHistoryFromPickle(self.fileNames.sixMonthsHistFileName)
        self.oneYearData = readHistoryFromPickle(self.fileNames.oneYearHistFileName)
        self.figOneYear = None
        self.figSixMonths = None

    def getSymbols(self):
        return list(self.sixMonthsData.columns.levels[0])

    def getDataBetweenDates(self,startDate,endDate):
        pass

    def viewData(self,showFig=False):
        self.figSixMonths = self._showData(self.sixMonthsData, title="6",showFig=showFig)
        self.figOneYear = self._showData(self.oneYearData, title="12",showFig=showFig)

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
        fig.update_layout(title=f"NIFTY 100 {title} Month History Data", showlegend=False)
        # fig.update_layout(height=1200 * 8, width=1400)
        fig.update_layout(height=1200 * 8, width=1500)
        if showFig:
            fig.show()
        return fig


if __name__ == '__main__':
    nifty100 = Nifty100()
    print(nifty100.sixMonthsData.tail())
    # nifty100.viewData()
    # nifty50.viewData()