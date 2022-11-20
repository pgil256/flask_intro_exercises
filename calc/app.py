# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    '''Return a+b.'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a,b)
    return str(sum)

@app.route('/sub')
def do_sub():
    '''return a-b'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    difference = sub(a,b)
    return str(difference)

@app.route('/mult')
def do_mult():
    '''return a*b'''

    a = int(request.args.get('a'))
    b = int(request.arge.get('b'))
    mult = mult(a,b)
    return str(mult)

@app.route('div')
def do_mult():
    '''return a/b'''
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    div = div(a,b)
    return str(div)