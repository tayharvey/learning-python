from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/add/<number_one>/<number_two>')
def add_two_numbers(number_one, number_two):
    '''
    Adds two integers, and returns the result as a string
    -
    number_one: str, to be added to number_two
    number_two: str, to be added to number_one
    '''
    return str(int(number_one) + int(number_two))

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))


if __name__ == '__main__':
    app.run(debug = True)
