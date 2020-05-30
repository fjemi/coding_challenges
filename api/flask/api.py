from flask import Flask, jsonify
from dataclasses import dataclass


app = Flask(__name__)


@dataclass
class Hello:
  text: str = 'Hello World!'


@app.route('/api'`)
def hello():
  return jsonify(Hello())
    

if __name__ == '__main__':
  app.run(debug=True, port=8080)
