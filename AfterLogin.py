from flask import Flask, render_template, request, session
from wtforms import Form, StringField, SelectField, validators
import Process
import datetime


app = Flask(__name__)


@app.route('/' , methods=['GET', 'POST'])
def home():
    session['userid'] = 'John'
    form = MonthForm(request.form)
    if request.method == 'POST' and form.validate():
        monthMM = form.month.data
        checkMonth = int(monthMM)
        print(monthMM)

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')

    if todayMonth == 1:
        prevMonth = 12
    else:
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1

    usersList = []
    usersList = Process.processUser(session['userid'], todayMonth)
    savings = []
    limit = []
    limit = Process.limit(session['userid'],todayMonth)
    over = Process.over(session['userid'],todayMonth)
    interest = Process.interest(session['userid'],todayMonth)
    return render_template('homepage.html', users=usersList,checkMM=months[todayMonth],saving=savings,todayMonth=todayMonth, prevMonth=prevMonth, todayYear=todayYear, prevYear=prevYear,limits=limit,over=over,form=form,interest=interest)

@app.route('/hey')
def hey():
    return render_template('homepage2.html')


@app.route('/dec')
def dec():
    session['userid'] = 'Mary'

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January','February','March','April','May','June','July','August','September','October','November','December')

    if todayMonth == 1:
        prevMonth = 12
    else :
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1
    usersList = []
    usersList = Process.processUser(session['userid'],prevMonth)
    limit = []
    limit = Process.limit(session['userid'], prevMonth)
    over = Process.over(session['userid'], prevMonth)

    return render_template('dec.html',users=usersList,todayMonth=todayMonth, prevMonth=prevMonth, todayYear=todayYear, prevYear=prevYear,limits=limit,over=over)


class MonthForm(Form):
    month = SelectField('Month', [validators.DataRequired()],
                           choices=[('', 'Select'), ('12', 'December'), ('11', 'November'),
                                    ('10', 'October'), ('9', 'September'), ('8', 'August'), ('7', 'July')],
                           default='')

@app.route('/selected', methods=['GET', 'POST'])
def selected():
    session['userid'] = 'John'

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    if todayMonth == 1:
        prevMonth = 12
    else :
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1
    form = MonthForm(request.form)
    if request.method == 'POST' and form.validate():
        monthMM = form.month.data
        checkMonth = int(monthMM)
        print(monthMM)

        months = ('Null','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')

        usersList = []

        usersList = Process.processUser(session['userid'], checkMonth)
        limit = []
        limit = Process.limit(session['userid'], checkMonth)
        over = Process.over(session['userid'], checkMonth)
        interest = Process.interest(session['userid'],checkMonth)

        return render_template('nov.html',users=usersList,checkMM=months[checkMonth], count=len(usersList),limits=limit,over=over,form=form,interest=interest)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()

