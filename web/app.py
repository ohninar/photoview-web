from flask import Flask, render_template, request, session, redirect, url_for

from web import config, backend

app = Flask(__name__)
app.config["SECRET_KEY"] = config.secret_key


@app.route("/")
def main():
    if session.get('token'):
        list_photos = backend.get_photos(session['token'])
        return render_template(
            "gallery.html",
            list_photos=list_photos,
        )
    else:
        return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        token = backend.login(email, password)
        session["token"] = token
        return redirect(url_for('main'))

    return render_template(
        "login.html"
    )


@app.route("/logout", methods=["GET"])
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        backend.signup(name, email, password)
        return redirect(url_for('login'))

    return render_template(
        "signup.html"
    )


@app.route("/upload", methods=["GET"])
def upload():
    return render_template("upload.html")


@app.route("/pendent", methods=["GET"])
def pendent():
    if session.get('token'):
        list_photos = backend.get_photos_pendent(session['token'])
        return render_template(
            "pendent.html",
            list_photos=list_photos,
        )
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)