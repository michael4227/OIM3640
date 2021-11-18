import re
from flask import Flask
app = Flask(__name__)

# @app.route('/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     if name:
#         return f'hellow, {name}'
#     return 'Hello, world!'

@app.route('/')
@app.route('/square/<num>')
def square(num=None):
    if num:
        return f'The square of the number is {int(num)**2}'
    return 'There is no number'


if __name__=='__main__':
    app.run(debug=True)