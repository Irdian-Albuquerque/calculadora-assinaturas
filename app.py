from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None

    if request.method == "POST":

        numero1 = float(request.form["numero1"])
        numero2 = float(request.form["numero2"])

        resultado = numero1 + numero2

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)