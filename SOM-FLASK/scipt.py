from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gas/')
def gas():
    return render_template('gas.html')

@app.route('/solid/')
def solid():
    return render_template('solid.html')

@app.route('/liquid/')
def liquid():
    return render_template('liquid.html')

@app.route('/plasma/')
def plasma():
    return render_template('plasma.html')

if __name__ == '__main__':
    app.run()
