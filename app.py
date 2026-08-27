from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = "chave-secreta-do-projeto"


@app.route("/", methods=["GET", "POST"])
def inicio():

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

        session["resultado"] = resultado

        return redirect(url_for("planos"))

    return render_template("index.html", resultado=None)


@app.route("/planos")
def planos():
    return render_template("planos.html")


@app.route("/escolher-plano", methods=["POST"])
def escolher_plano():

    plano = request.form["plano"]

    session["plano"] = plano

    return redirect(url_for("pagamento"))


@app.route("/pagamento", methods=["GET", "POST"])
def pagamento():

    plano = session.get("plano")

    if plano == "padrao":
        nome_plano = "Padrão"
        preco = "19,90"

    elif plano == "premium":
        nome_plano = "Premium"
        preco = "49,90"

    elif plano == "elite_pro":
        nome_plano = "Elite Pro"
        preco = "99,90"

    else:
        return redirect(url_for("planos"))

    if request.method == "POST":

        session["pagamento_aprovado"] = True

        return redirect(url_for("resultado"))

    return render_template(
        "pagamento.html",
        nome_plano=nome_plano,
        preco=preco
    )

@app.route("/resultado")
def resultado():

    pagamento_aprovado = session.get("pagamento_aprovado")

    if not pagamento_aprovado:
        return redirect(url_for("planos"))

    resultado_calculo = session.get("resultado")
    plano = session.get("plano")

    if plano == "padrao":
        nome_plano = "Padrão"

    elif plano == "premium":
        nome_plano = "Premium"

    elif plano == "elite_pro":
        nome_plano = "Elite Pro"

    else:
        return redirect(url_for("planos"))

    return render_template(
        "resultado.html",
        resultado=resultado_calculo,
        nome_plano=nome_plano
    )

if __name__ == "__main__":
    app.run(debug=True)