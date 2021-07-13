from flask import Flask, render_template

app = Flask(__name__)


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi {0}".format(name)

@app.route('/repeat/<int:rep>/<noun>')
def repeat(rep, noun):
    return "{0}".format(noun) * rep

@app.route('/play/<int:x>/<color>')
def play(x,color):
    return render_template('index.html', num = x, color=color)

@app.route('/play/<int:x>')
def play1(x):
    return render_template('index.html', num = x)

@app.route('/')
def normal():
    return render_template('checkerboard.html')

@app.route('/<int:x>')
def check(x):
    return render_template('checkerboard.html', num1 = x)

@app.route('/<int:x>/<int:y>')
def checker(x,y):
    return render_template('checkerboard.html', num1 = x, num2 = y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard(x,y,color1, color2):
    return render_template('checkerboard.html', num1 = x, num2 = y, color1=color1, color2=color2)

@app.route('/users')
def users():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('table.html', users = users)


if __name__ == "__main__":
    app.run(debug = True)