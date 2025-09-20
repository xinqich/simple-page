from flask import redirect, render_template, request, url_for
from datetime import datetime

from app import app


@app.route("/")
def home():
    return render_template("index.html", time=datetime.now())


@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team=team_members)


@app.route("/contact")
def contact():
    customer_care = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031",
        "website": "hildegard.org",
    }
    return render_template("contact.html", customer_care=customer_care)


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        user = request.form.to_dict()
        return render_template('result.html', user=user)
    else:
        return redirect(url_for("contact"))
