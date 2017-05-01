from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
from sequence_generators import fibonacci


def make_json_app():
    """
    Creates a JSON-oriented Flask app.
    All error responses will contain JSON like this (just an example):
    { "message": "405: Method Not Allowed" }
    """

    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    application = Flask(__name__)

    for code in default_exceptions.keys():
        application.error_handler_spec[None][code] = make_json_error

    return application


application = make_json_app()


@application.route('/fibonacci/<int:size>')
def fibonacci_sequence(size):
    if size > 1000:
        response = jsonify(message=('Size must be a positive integer '
                                    '<= to 1000. Actual %s' % size))
        response.status_code = 400
        return response

    return jsonify(fibonacci=fibonacci.generate_sequence(size))


@application.route('/fibonacci/<invalid_path>')
def handle_invalid_path(invalid_path):
    response = jsonify(message=('Size must be a positive integer. '
                                'Actual %s' % invalid_path))
    response.status_code = 400
    return response


if __name__ == '__main__':
    application.run(debug=True)
