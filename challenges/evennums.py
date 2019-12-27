"""
Model to determine the number of even integers between two numbers a,b 
"""

# data object modeling
from dataclasses import dataclass, field, asdict
from typing import List, Dict
# time
import time
from datetime import datetime
# data storage
import json

@dataclass
class Input:
    '''Input data object model'''
    a: int
    b: int
    error: str = field(default=None, init=False)
    
    
    def __post_init__(self):
        '''Validate data after initilization'''
        try: 
            self.a, self.b = int(self.a), int(self.b)
            
        except:
            self.error = 'Invalid input data type'


@dataclass
class Model:
    '''Object model for keeping track of even numbers'''
    input_data: Dict
    output_data: List[int] = field(default_factory=list)
    error: str = field(default=None, init=False)
    created: str = field(default_factory=lambda: datetime.utcnow())
    runtime: int = None
    
    
    def __post_init__(self):
        '''Function that lists even numbers between two integers, a and b, inclusively'''
        try:
            print(self.input_data['error'])
            if self.input_data['error'] is not None:
                raise Exception('Invalid input data type')
                pass
            
            # check if a,b are integers and b > a
            if int(self.input_data['a']) > int(self.input_data['b']):
                raise Exception('a > b for integers a, b')
            
            for i in range (self.input_data['a'], self.input_data['b'] + 1):
                if i % 2 == 0:
                    self.output_data.append(i)
            
        except Exception as e:
            self.error = str(e)
            
        finally:
            # cacluate the function runtime
            self.runtime = (datetime.utcnow() - self.created).total_seconds()
            # Convert datetime to string. Datetime is not JSON serializable
            self.created = self.created.strftime('%Y%m%d.%H%M%S')
            
    
    def get_var(self, var_name):
        '''Returns data of a class variable in JSON format'''
        # Check if var name is valid
        var = None
        if var_name in vars(self).keys():
            var = vars(self)[var_name]
        return json.dumps({var_name: var}, indent=2)
    

if __name__ == '__main__':
    data = [(1, 7), ('s', 'a')]
    
    for d in data:
        i = Input(d[0], d[1])
        i = asdict(i)
    
        e = Model(i)
        print(json.dumps(asdict(e), indent=2))
