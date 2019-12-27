# web development
from fastapi import FastAPI
import uvicorn
#from flask import jsonify
# data modeling
from dataclasses import dataclass, asdict

# create FastAPI instance
app = FastAPI()


@dataclass
class Hello:
    text: str = 'Hello World!'
    

@app.get('/', methods=['GET'])
async def hello():
    return Hello() #jsonify(Hello())


if __name__ == '__main__':
    uvicorn.run(app, debug=True, port=8082)
