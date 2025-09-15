from flask import redirect, render_template, request, url_for

from app import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get('message')
        return render_template('result.html', name=name, email=email, message=message)
    else:
        return redirect(url_for("contact"))
