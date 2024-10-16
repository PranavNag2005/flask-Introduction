from flask import Flask  

app=Flask(__name__)
@app.route('/')

def index():
    return "<h1>Hello and welcome to flask</h1>"

@app.route('/abc')
def Hello():
    return "welcome to flask pranav"

# dynamic urls
@app.route('/greet/<name>')
def greet(name):
    return f"Hello,{name}"

# sum of two numbers using an flask application
@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1} + {number2}={number1 + number2}'
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)