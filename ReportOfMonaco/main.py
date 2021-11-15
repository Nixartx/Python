from ReportMonaco import ReportMonaco
from CLReportMonaco import CLReportMonaco

if __name__=="__main__":
    #R=CLReportMonaco()
    CLReportMonaco().run()
    #R.run()
    #R.run(['--files', 'reports', '--desc'])
    #R.run(['--files', 'reports', 'driver', 'Daniel Ricciardo'])
    #R.run(['--files', 'reports', '--asc'])
    ReportMonaco().print_report(folder='reports', driver_name="Daniel Ricciardo")
