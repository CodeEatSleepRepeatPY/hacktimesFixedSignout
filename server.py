from flask import Flask, render_template, request,redirect,url_for, session
import database
import utils

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if session.get('logged_in'):
            return render_template("index.html",signout="Signout")
        else:
            return render_template("index.html")
    else:
        provided_username = request.form['username']
        provided_password = request.form['password']

        if database.validate(provided_username, provided_password):
            session['logged_in'] = True
            return redirect(url_for('blog'))#'Logged in as admin' render_template('index.html', loggedIn=loggedIn)
        else:
            return 'Incorrect username or password'

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if session.get('logged_in'):
            return render_template('Register.html',signout='Signout')
        else:
            return render_template('Register.html')
    else:
        provided_username = request.form['username']
        provided_password = request.form['password']
        database.add(provided_username, provided_password)

        return redirect(url_for('index'))

@app.route("/blog")
def blog():
    if session.get('logged_in'):
        return render_template("Blog.html",signout='Signout')
    else:
        return 'You need to be logged in to view this page'

@app.route("/contact")
def contact():
    if session.get('logged_in'):
        return render_template("Contact.html",signout='Signout')
    else:
        return render_template("Contact.html")

@app.route("/about")
def about():
    if session.get('logged_in'):
        return render_template("About.html",signout='Signout')
    else:
        return render_template("About.html")

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = 'qbnebYFQYbyebyBBs'
    app.run(debug=True)
