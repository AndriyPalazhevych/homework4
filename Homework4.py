from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    square = cube = mod5 = None
    if request.method == "POST":
        try:
            a = int(request.form.get("a"))
            square = a ** 2
            cube = a ** 3
            mod5 = a % 5
        except:
            pass
    return render_template("index.html", square=square, cube=cube, mod5=mod5)

if __name__ == "__main__":
    app.run(debug=True)