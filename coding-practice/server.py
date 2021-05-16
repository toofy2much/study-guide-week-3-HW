from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/results')
def show_results():
    cheery = request.arg.get('cheery')
    honest =request.arg.get('honest')
    dreary = request.arg.get('dreary')

    if cheery:
        msg = "pin a rose on your nose"
    if honest:
        msg = "your no Pinochio"
    if dreary:
        msg = "tomorow is a new day"

    return render_template('results.html', msg=msg)

@app.route('/save-name' ,methods= ["Post"])
def save_name():
    name = request.form.get('name')
    session['name'] = name
    return render_template('/save-name' ,methods = ["Post"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
