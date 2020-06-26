import imdb
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    lis = imdb.movie_info()
    return render_template('home.html', data=lis)


app.run(debug=True)