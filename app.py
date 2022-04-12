from flask import Flask, session, render_template, request, flash
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.debug = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
toolbar = DebugToolbarExtension(app)

rates = CurrencyRates()

code = CurrencyCodes()

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/convert', methods=["POST"])
def convert():
    top = request.form['topText'].upper()
    mid = request.form['middleText'].upper()
    symbol = code.get_symbol(mid)
    bottom = None
    answer = None
    err = None
    try:
        bottom = int(request.form['bottomText'])
        answer =  round(rates.convert(top, mid, bottom), 2)
    except(RatesNotAvailableError, ValueError) :
        if isinstance(bottom, int):
            answer = answer
        if isinstance(bottom, int) == False:
            err = 'Amount must be an integer'
        if code.get_symbol(top) == None:
            err = f"Currency {top} not supported"
        elif code.get_symbol(mid) == None:
            err = f"Currency {mid} not supported"    
    return render_template('convert.html', answer=answer, symbol=symbol, err=err)


    


    
