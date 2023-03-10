import os.path

from nifty50.reader import Nifty50
from nifty100.reader import Nifty100
from nifty200.reader import Nifty200

def saveFigures(niftyObjects):
    _output_dir_path = niftyObjects[0].fileNames.sixMonthsHistFileName.rsplit('\\',2)[0]+os.path.sep+\
                       'output_figs'+os.path.sep
    _figs_html_files_dir = niftyObjects[0].fileNames.sixMonthsHistFileName.rsplit('\\',2)[0]+os.path.sep+\
                       'figs_of_html'+os.path.sep
    for obj in niftyObjects:
        if obj.figSixMonths is None:
            print("No Figures Found...")
            break
        # _pdfFileName = os.path.split(obj.fileNames.sixMonthsHistFileName)[1].replace('.pkl','.pdf')
        # obj.figSixMonths.write_image(_output_dir_path+_pdfFileName)
        _htmlFileName = os.path.split(obj.fileNames.sixMonthsHistFileName)[1].replace('.pkl','.html')
        with open(_figs_html_files_dir+_htmlFileName,"w") as fp:
            fp.write(obj.figSixMonths.to_html())
        # _pdfFileName = os.path.split(obj.fileNames.oneYearHistFileName)[1].replace('.pkl', '.pdf')
        # obj.figOneYear.write_image(_output_dir_path+_pdfFileName)
        _htmlFileName = os.path.split(obj.fileNames.oneYearHistFileName)[1].replace('.pkl', '.html')
        with open(_figs_html_files_dir + _htmlFileName,"w") as fp:
            fp.write(obj.figOneYear.to_html())

n50 = Nifty50()
n100 = Nifty100()
n200 = Nifty200()
# print(n50.fileNames.sixMonthsHistFileName.rsplit('\\',2)[0]+os.path.sep+'output_figs'+os.path.sep)
n50.viewData(showFig=True)
n100.viewData()
n200.viewData()
# #
saveFigures([n50,n100,n200])


