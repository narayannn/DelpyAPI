from flask import Flask , request , jsonify
from src.lyrics import lyrics


app = Flask(__name__)

@app.route("/lyrics")
def lyr():
    query = request.args.get("q")
    data = lyrics(query)
    return jsonify(data)

