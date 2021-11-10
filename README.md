# Reference embedding server

Flask server to calculate embeddings (feature vectors) for given input sentences. Uses the [SentenceTransformers](https://www.sbert.net/) library. Returns the vectors as raw float-32-encoded bytes in the response body.

## Installation

Install the `pipenv` program to manage the Python packages. Then run `pipenv install`.

To run the server, run:

    pipenv run flask run

Now visit http://localhost:5000/encode?q=hello+world to encode sentences.
