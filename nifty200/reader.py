from maintenance import NIFTY200_HistoryFileNames,calculate_time,readHistoryFromPickle
class Nifty200:
    def __init__(self):
        self.fileNames = NIFTY200_HistoryFileNames()
        self.sixMonthsData = readHistoryFromPickle(self.fileNames.sixMonthsHistFileName)
        self.oneYearData = readHistoryFromPickle(self.fileNames.oneYearHistFileName)

    def getSymbols(self):
        return list(self.sixMonthsData.columns.levels[0])

    def getDataBetweenDates(self,startDate,endDate):
        pass

    def viewData(self):
        self._showData(self.sixMonthsData,title="6")
        self._showData(self.oneYearData,title="12")

    @staticmethod
    def _showData(df, title):
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
        fig.show()


if __name__ == '__main__':
    nifty200 = Nifty200()
    nifty200.viewData()
    # nifty50.viewData()