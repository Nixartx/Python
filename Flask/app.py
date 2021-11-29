from flask import Flask, render_template,request
from ReportOfMonaco import ReportMonaco


app=Flask(__name__)


@app.route('/')
@app.route('/report')
def report():
    data=ReportMonaco().print_report(folder='static/reports')
    return render_template('report.html',data=data)


@app.route('/report/drivers', methods=['GET'])
def list():
    driver_id=request.args.get('driver_id')
    order=request.args.get('order')
    if driver_id:
        return render_template('report.html')
    return render_template('list.html')

@app.template_filter()
def format_datetime(value):
    return str(value)[:-3]

if __name__=="__main__":
    app.run(debug=True)
