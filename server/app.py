#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# print route string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter) # displays parameter in console
    return parameter # displays parameter in browser

# count route
@app.route('/count/<int:parameter>')
def count(parameter):
    count = f''
    for i in range(parameter):
        count += f"{i}\n"
    return count

# math route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Error :Invalid operation'
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Invalid operation'

    return str(result)
    

