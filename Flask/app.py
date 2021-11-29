from flask import Flask, render_template,request
from ReportOfMonaco import ReportMonaco


app=Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/report/', methods=['GET'])
def report():
    order = request.args.get('order')
    if order and order.upper()=='DESC':
        order=True
    else:
        order=False

    data=ReportMonaco().print_report(folder='static/reports',reverse=order)
    return render_template('report.html',data=data)


@app.route('/report/drivers/', methods=['GET'])
def list():
    driver_id=request.args.get('driver_id')
    order=request.args.get('order')
    if order and order.upper()=='DESC':
        order=True
    else:
        order=False

    if driver_id:
        #Finds full name of driver
        rmobj=ReportMonaco().build_report('static/reports')
        driver_name=rmobj.report.get(driver_id)['fullname']

        data = rmobj.print_report(folder='static/reports', driver_name=driver_name, reverse=order)
        return render_template('report.html', data=data)

    data=ReportMonaco().print_report(folder='static/reports', reverse=order)
    return render_template('list.html',data=data)

@app.template_filter()
def format_datetime(value):
    return str(value)[:-3]

if __name__=="__main__":
    app.run(debug=True)
