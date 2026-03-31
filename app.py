from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# データ保存（簡易）
data_list = []

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/api", methods=["POST"])
def receive():
    data = request.json

    print("受信:", data)

    data_list.append(data)

    return jsonify({"status": "ok"})

@app.route("/data")
def get_data():
    return jsonify(data_list)

if __name__ == "__main__":
    app.run()