from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bye", methods=["GET"])
def bye():
	return jsonify(f"reply from endpoint bye")

@app.route("/hello", methods=["GET"])
def hello():
	return jsonify(f"reply from endpoint hello")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)