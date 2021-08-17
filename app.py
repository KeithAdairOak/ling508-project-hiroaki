from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

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
cors = CORS(app, resources={r"/pronounce": {"origins": "http://localhost:63342"}})
services = Services()


@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()


@app.route("/pronounce", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def pronounce():
    data = request.get_json()
    app.logger.info(f"/parse - Got request: {data}")
    main.sound(data.get('word'))
    return jsonify({"msg": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
