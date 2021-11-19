from ReportOfMonaco.src.ReportMonaco import ReportMonaco
from ReportOfMonaco.src.CLReportMonaco import CLReportMonaco

if __name__=="__main__":
    #R=CLReportMonaco()
    #CLReportMonaco().run()
    #R.run()
    #R.run(['--files', 'reports', '--desc'])
    #R.run(['--files', 'reports', 'driver', 'Daniel Ricciardo'])
    #R.run(['--files', 'reports', '--asc'])
    #ReportMonaco().print_report(folder='reports', driver_name="Daniel Ricciardo")
    #ReportMonaco().print_report(folder="./tests/reports", driver_name=" Ricciardo")
    CLReportMonaco().run(['--files', './tests/reports', 'driver', 'Daniel Ricciardo'])
