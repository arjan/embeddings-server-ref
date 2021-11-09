from flask import Flask, request, make_response
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
model = SentenceTransformer('all-mpnet-base-v2')

@app.route("/encode", methods=["GET", "POST"])
def encode():
  q = request.args.get('q')
  if q:
    sentences = q
  else:
    sentences = request.form.getlist('q')
  vector = model.encode(sentences)
  response = make_response(vector.tobytes())
  response.headers.set('Content-Type', 'application/octet-stream')
  return response
