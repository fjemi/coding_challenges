from flask import jsonify
from flask_api import FlaskAPI

from dataclasses import dataclass


app = FlaskAPI(__name__)


@dataclass
class Hello:
    text: str = 'Hello World!'


@app.route('/api', methods=['GET'])
def hell():
    return jsonify(Hello())


if __name__ == '__main__':
    app.run(debug=True)
