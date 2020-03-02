from app import app

from flask import Flask, render_template, request, redirect, jsonify, make_response, flash, url_for, send_from_directory

from datetime import datetime

from werkzeug.utils import secure_filename


import os

UPLOAD_FOLDER = 'C:/uploads'
ALLOWED_EXTENSIONS = set(['csv', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")


@app.route("/")
def index():
    return render_template("public/index.html")
    #return "Message1" #app.config["MESSAGE"]

@app.route("/jinja")
def jinja():

    my_name = "Luke"

    age = 21

    langs = ["Python", "JavaScript", "Bash", "C#"]

    friends = {
        "Tom": 30,
        "Amy": 60,
        "Tony": 56,
        "Clarissa": 23
    }

    colours = {"Red", "Green"}

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    
    my_remote = GitRemote(
        name="Flask Jinja",
        description="Template design tutorial",
        url="https://github.com/LukeRaw/flaskCourse.git"
    )
        

    def repeat(x,qty):
        return x * qty

    date = datetime.utcnow()

    my_html = "<h1>THIS IS SOME HTML</h1>"

    suspicious = "<script>alert('YOU GOT HACKED')</script>"

    return render_template("public/jinja.html", my_name=my_name, age=age,
    langs=langs, friends=friends, colours=colours, cool=cool,
    GitRemote=GitRemote, repeat=repeat, my_remote=my_remote, date=date,
    my_html=my_html, suspicious=suspicious
    )

@app.route("/about")
def about():
    return render_template("public/about.html")
    #return "<h1 style='color: red'>About!!!!</h1>"

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req["username"]
        email = req.get("email")
        password = request.form["password"]

        print(username, email, password)

        return redirect(request.url)

    return render_template("public/sign_up.html")

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creator of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum":{
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html", username=username, user=user)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["POST"])
def json():

    if request.is_json:

        req = request.get_json()

        response = {
            "message": "JSON received!",
            "name": req.get("name")
        }

        res = make_response(jsonify(response), 200)

        return res

    else:

        res = make_response(jsonify({"message": "No JSON received"}), 400)

        return res


@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    return "Thanks"
