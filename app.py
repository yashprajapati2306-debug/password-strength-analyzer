from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_strength(password):
    score = 0

    # Length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        password = request.form["password"]
        result = check_strength(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)