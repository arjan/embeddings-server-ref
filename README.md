# Reference embedding server

Servers encoding embeddings (feature vectors) for given input sentences.

## Installation

Install the `pipenv` program to manage the Python packages. Then run `pipenv install`.

To run the server, run:

    pipenv run flask run

Now visit http://localhost:5000/encode?q=hello+world to encode sentences.
