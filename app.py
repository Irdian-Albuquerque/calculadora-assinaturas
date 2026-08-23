from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None

    if request.method == "POST":

        numero1 = float(request.form["numero1"])
        numero2 = float(request.form["numero2"])
        operacao = request.form["operacao"]

        if operacao == "+":
            resultado = numero1 + numero2

        elif operacao == "-":
            resultado = numero1 - numero2

        elif operacao == "*":
            resultado = numero1 * numero2

        elif operacao == "/":

            if numero2 != 0:
                resultado = numero1 / numero2

            else:
                resultado = "Não é possível dividir por zero."

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)