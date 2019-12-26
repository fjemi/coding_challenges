# data analysis
import json
import pandas as pd
# class object models
from dataclasses import dataclass, field, asdict
from typing import List, Dict
#from types import SimpleNamespace
# date/time
import calendar
from dateutil.parser import parse
from datetime import datetime, date


@dataclass(order=True)
class Birthdate:
    '''Object model for storing input data'''
    year: int   
    month: int
    day: int
    
    
    def __post_init__(self):
        ''''''
        pass
    
    
@dataclass(order=True)
class Birthdays:
    '''Object model for storing output data'''
    date: datetime = None  
    day: str = None
    
  
@dataclass(order=True)
class Model:
    '''Object model for keeping track of birthdays'''
    birthdate: Dict
    birthdays: List[Birthdays] = field(default_factory=list)
    count: Dict[str, int] = field(default_factory=dict)
    created: datetime = field(default_factory=lambda: datetime.utcnow())
    runtime: int = None
    error: str = None
    
    
    def __post_init__(self):
        '''Perform tasks after object initialization'''
        
        try:
            if self.birthdate == None:
                raise Exception('Error: No data passed to the class')
            
            # start/end year to iterate through
            a = self.birthdate['year']
            b = int(self.created.strftime('%Y'))
            
            # List the birthdates since the original
            for i in range (a, b + 1):                 
                _date = date(i, self.birthdate['month'], self.birthdate['day'])
                weekday = _date.strftime('%a')
                _date = _date.strftime('%G%m%d')
                data = {'date': _date, 'weekday': weekday}
                self.birthdays.append(data)
                
                # Use a dictionary to keep count of days
                if weekday in self.count.keys(): 
                    self.count[weekday] = self.count[weekday] + 1
                else:
                    self.count[weekday] = 1
                    
        except Exception as e:
            self.error = str(e)
    
        finally:
            # Set function runtime
            self.runtime = (datetime.utcnow() - self.created).total_seconds()
            # Convert datetime to string. Datetime is not JSON serializable
            self.created = self.created.strftime('%Y%m%d.%H%M%S')
            
            
    def get_count(self):
        '''Returns weekday counts in JSON format'''
        count = self.count
        
        return json.dumps(count, indent=2)
           

if __name__ == '__main__':
    b = Birthdate(1985, 5, 7)
    # Convert class object to dictionary
    b = asdict(b)          

    m = Model(b)
    d = asdict(m)
    # Convert dictionary object to JSON
    print(json.dumps(d, indent=2))
    
