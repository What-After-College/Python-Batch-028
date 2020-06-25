from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<h1>hii, hello</h1>"

@app.route("/")
def home():
    my_dic={
        "name" : "adwaita",
        "year" : "4rth"
    }
    return my_dic

# @app.route("/welcome")
# def welcome():
#     return "<h1>hii adwaita</h1>"

@app.route("/<name>")
def welcome(name):
    return "hello" + str(name)


app.run(debug=True, port=5001)