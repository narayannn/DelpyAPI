from flask import Flask , request , jsonify , render_template
from src.lyrics import lyrics



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("./home/index.html")

@app.route("/lyrics")
def lyr():
    query = request.args.get("q")
    data = lyrics(query)
    return jsonify(data)

