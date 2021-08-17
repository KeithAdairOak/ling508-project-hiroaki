from typing import Any
from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)

    # This list will store the data
    data = [{"id": 1, "first_name": "John", "last_name": "Smith"}]

    # A simple example of how to do a GET method
    @app.route("/hello", methods=["GET"])
    def hello():
        return "Hello World!"

    # Implement a GET method called "/get_data" that returns the contents of data as a JSON string
    # '/get_data' goes here:
    @app.route("/get_data", methods=["GET"])
    def get_data():
        return jsonify(data)

    # Implement a POST method called "/post_data" that takes a JSON string and adds it to data. It should return
    # a JSON string like this '{"msg": "success"}' if everything worked.
    # '/post_data' goes here:
    @app.route("/post_data", methods=["POST"])
    def post_data():
        data.append(request.get_json())
        return jsonify({"msg": "success"})

    return app


if __name__ == "__main__":
    myapp = create_app()
    myapp.run()
