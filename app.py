from flask import Flask, redirect, render_template, url_for


app = Flask(__name__)


@app.route("/")
def home():
    """Render the portfolio home page."""
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/skills")
def skills():
    return redirect(url_for("home", _anchor="skills"))


@app.route("/contact")
def contact():
    return redirect(url_for("home", _anchor="contact"))


if __name__ == "__main__":
    app.run(debug=True)
