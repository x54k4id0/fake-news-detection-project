from flask import Flask, jsonify
from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)


@app.route("/postrand", methods=['GET', 'POST'])
def postrand():
    return jsonify({"response":"reponse", "percent":"99%"})

if __name__ == "__main__":
    port=os.environ.get("PORT",3000)
    app.run(host="0.0.0.0", port=port, debug=False)