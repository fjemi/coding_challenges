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
class Data:
    '''Object model for storing input/output data'''
    # attributes
    birthdate: None
    output: None

    
@dataclass(order=True)
class Birthdate:
    '''Object model for storing input data'''
    year: int   
    month: int
    day: int
    
    
@dataclass(order=True)
class Birthdays:
    '''Object model for storing output data'''
    date: datetime = None  
    day: str = None
    
  
@dataclass(order=True)
class Birthdays:
    '''Object model for keeping track of birthdays'''
    birthdate: Dict
    birthdays: List[Birthdays] = field(default_factory=list)
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
                data = {'date': _date, 'weekday': weekday}
                self.birthdays.append(data)
                
            for item in self.birthdays:
                # Convert the dictionary to 
                #item = SimpleNamespace(**item)
                print(item)

        except Exception as e:
            self.error = str(e)
    
        finally:
            # Set function runtime
            self.runtime = (datetime.utcnow() - self.created).total_seconds()
            
    #def get():
        
    

class Birthday():
    '''Class that determines the days that a person's brithday has fallen on from birth'''
    
    def __init__(self, data):
        '''Initialize the class.'''
        self.data = data
        
        
    @staticmethod
    def calculate(data):
        '''Determine the day associated with each birthday from the day of birth to the current year'''
        try:
            
            birthdays = [] # List to store the birthdays

            end_year = int(datetime.utcnow().strftime('%Y'))
            weekends = {}
            
            # IterateBackup_ through the current/birth years and set the birth date/day
            for year in range(data['year'], end_year):
                birthdate = date(year, data['month'], data['day']) 
                birthday = birthdate.strftime('%A')
                # Convert to a string since dates are not serializable JSON objects
                birthdate = birthdate.utcnow()
                birthdays.append({'birthdate': birthdate, 'birthday': birthday})
                
                # Count the number of birthdays falling on a weekend
                if birthday in weekends.keys():
                    weekends[birthday] = weekends[birthday] + 1
                else:
                    weekends[birthday] = 1
                
            data['birthdays'] = birthdays
            data['weekends'] = weekends
            
        except Exception as e:
            data['error'] = e.__str__()
            
        return json.dumps(data)
           

if __name__ == '__main__':
    b = Birthdate(1985, 5, 7)
    # convert dataclass to a dictionary
    b = asdict(b)          

    b = Birthdays(b)
    b = asdict(b)
    print(b)
