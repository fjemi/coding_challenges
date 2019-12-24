# data analysis
import json
import pandas as pd
# class object models
from dataclasses import dataclass, field
from typing import List, Dict
from dataclasses_json import dataclass_json
# datetime
import calendar
from dateutil.parser import parse
from datetime import datetime, date


@dataclass_json
@dataclass(order=True)
class Date:
    '''Object model for storing date information'''
    
    # attributes
    year: int   
    month: int
    day: int
    
  
@dataclass_json
@dataclass(order=True)
class Birthdays:
    '''Object model for keeping track of birthdays'''
    birthdays : List[Date]
    created: datetime = field(default_factory=lambda: datetime.utcnow())
    runtime: int = None
    error: str = None
    
    
    def __post_init__(self):
        '''Perform tasks after object initialization'''
        try:
            if self.birthdays == []:
                raise Exception('Error: An empty list was passed as an arguement')
            
            # iterate over years from birth. determine the day of birthdates
            a = self.birthdays[0].year
            b = self.created.year
            for i in range (a, b + 1):
                print(i, self.birthdays[0].month, self.birthdays[0].day)
            
            pass
    
        except Exception as e:
            self.error = str(e)
    
        finally:
            self.runtime = (datetime.utcnow() - self.created).total_seconds()
    

class Birthday():
    '''Class that determines the days that a person's brithday has fallen on from birth'''
    
    def __init__(self, data):
        '''Initialize the class.'''
        self.data = data
        
        
    @staticmethod
    def calculate(data):
        '''Determine the day associated with each birthday from the day of birth to the current year'''
        try:
            # List to store the birthdays
            birthdays = []

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
    data = {'month': 5, 'day': 7, 'year': 1985}
    bday = Birthday.calculate(data)
    #print(bday)
    data = {'month': 11, 'day': 30, 'year': 1992}
    bday = Birthday.calculate(data)
    #print(bday)
    
    
    d = Date(2015, 5, 6)
    print(d.to_json())
    
    b = Birthdays([Date(2015, 5, 6)])
    print(b)
    #b = Birthdays([])
    #print(b)
