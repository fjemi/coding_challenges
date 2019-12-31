# web development
from fastapi import FastAPI
import uvicorn
#from flask import jsonify
# data modeling
from dataclasses import dataclass, asdict, field
from typing import Any
# imports
#import importlib
# 
#import sys
#import os

    
@dataclass
class DynamicImport:
    '''
    module_path: path to the module
    class_name: name of the module class
    instance: an instance of the class
    '''
    module_path: str
    class_name: str
    instance: None
    
    
    def __post_init__(self):
        '''
        Returns instance of the module class
        '''
        module = __import__(self.module_path)
        class_ = getattr(module, self.class_name)
        self.instance = ''
     
    


# create FastAPI instance
app = FastAPI()


@dataclass
class Hello:
    text: str = 'Hello World!'
    

@app.get('/')
async def hello():
    return Hello() #jsonify(Hello())


#@app.get('/challenge/<challenge_name>')
#async def challenge(challenge_name):
    
    


if __name__ == '__main__':
    #uvicorn.run(app, debug=True, port=8082)
    module_path = 'birthdays.py'
    print(module_path)
    class_name = 'Model'
    d = DynamicImport(module_path, class_name)
    print(d)
