from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    user1 = ['neeraj','prakhar','adwaita','shivam']
    return render_template('home.html', user=user1)


@app.route("/welcome")
def welcome():
    return render_template('second.html')

@app.route("/user")
def user():
    user="adwaita"
    return render_template('dt.html',user=user)



app.run(debug=True, port=5001)