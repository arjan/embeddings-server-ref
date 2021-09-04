from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
model = SentenceTransformer('all-mpnet-base-v2')

@app.route("/encode")
def encode():
  sentence = request.args.get('q')
  return jsonify(model.encode(sentence).tolist())
