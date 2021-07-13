from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"


@app.route('/')
def index():
    if "user_gold" not in session:
        session['user_gold'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        session['user_gold'] += random.randint(10,20)
    if request.form['building'] == 'cave':
        session['user_gold'] += random.randint(5,10)
    if request.form['building'] == 'house':
        session['user_gold'] += random.randint(2,5)
    if request.form['building'] == 'casino':
        session['user_gold'] += random.randint(-50,50)
    
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)