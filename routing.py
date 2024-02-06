from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home Page</p>"

@app.route("/<name>")
def user(name):
    return f"<p>Hello, {name}!</p>"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="admin!"))

if __name__ == "__main__":
  app.run()