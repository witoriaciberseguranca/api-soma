from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/soma", methods=["GET"])
def soma():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None:
        return jsonify({"erro": "informe a e b, exemplo: ?a=2&b=3"}), 400

    return jsonify({"resultado": a + b})

@app.route("/api/soma", methods=["POST"])
def soma_post():
    dados = request.get_json(silent=True) or {}
    a = dados.get("a")
    b = dados.get("b")

    cliente = request.headers.get("X-Cliente", "anonimo")

    if a is None or b is None:
        return jsonify({"erro": "envie a e b no corpo JSON"}), 400

    return jsonify({"resultado": a + b, "chamado_por": cliente})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)