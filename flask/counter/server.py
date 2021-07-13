from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def count():
    if 'key_name' not in session:
        session['key_name'] = 0 
    session['key_name'] += 1
        

    return render_template('index.html')

@app.route("/destroy_session", methods=['POST'])
def destroy_session():
    session.clear()		# clears all keys
    #session.pop('key_name')		# clears a specific key
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)