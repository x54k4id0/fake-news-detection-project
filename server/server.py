from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import sys
import os



app = Flask(_name_)
CORS(app)

# Path for our main frontend page
@app.route("/")
def base():
    return send_from_directory('../fake-news-ai/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../fake-news-ai/public', path)



@app.route("/postrand", methods=['GET', 'POST'])
def postrand():
    import main

    news = request.get_json()["news"]
    print("Your news is : "+news)
    answer = main.getanswer(news)[0]
    print(answer)

    if "main" in sys.modules:
        del sys.modules["main"]


    return jsonify({"response":answer[0], "percent":str(answer[1]*100)[:4]+"%"})

if _name_ == "_main_":
    port=os.environ.get("PORT",3000)
    app.run(host="0.0.0.0", port=port, debug=False)
