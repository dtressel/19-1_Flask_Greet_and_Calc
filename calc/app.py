from flask import Flask, request

from operations import add, sub, mult, div, math

app = Flask(__name__)

@app.route('/add')
def respond_add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a, b)
    return str(result)

@app.route('/sub')
def respond_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def respond_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = str(mult(a, b))
    return str(result)

@app.route('/div')
def respond_div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a, b)
    return str(result)

@app.route('/math/<operation>')
def respond_math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = math(a, b, operation)
    return str(result)
