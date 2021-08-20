import os
from logging.config import dictConfig
import app
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/pronounce": {"origins": "http://localhost:port"}})
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:63342"}})


@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()


@app.route("/pronounce", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def pronounce():
    data = request.get_json()
    app.logger.info(f"/pronounce - Got request: {data}")
    services = Services(data.get('word'))
    filepath = services.pronounce()
    os.system('mpg123 "' + filepath + '"')
    os.system('rm "' + filepath + '"')

    return jsonify({"msg": "success"})

@app.route("/search", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def search():
    data = request.get_json()
    app.logger.info(f"/search - Got request: {data}")
    services = Services(data.get('word'))
    res = services.fetch()
    ret = [{"form": _.form, "pos": _.pos, "verb_class": _.verb_class, "noun_gender": _.noun_gender, \
            "origin_form": _.origin_form, "origin_lang": _.origin_lang} for _ in res][:1]

    return jsonify(ret)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
