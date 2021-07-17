from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process_survey", methods=['POST'])
def process():
    session['first_name'] = request.form['first_name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    return redirect("/result")


@app.route("/result")
def display():
    return render_template(
        "display.html",
        first_name = session['first_name'],
        dojo_location = session['dojo_location'],
        fav_language = session['fav_language'],
        comment = session['comment']
    )


if __name__=="__main__":
    app.run(debug=True)