#!usr/bin/env python3

from typing import List, Dict
from dataclasses import dataclass, field
from json import dumps


@dataclass
class Logger:
  # delete
  wait: int = -1  
  result: List[Dict] = field(default_factory=lambda: [])
  # keep
  logs: Dict[str, int] = field(default_factory=lambda: {})
  
  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    ''''''
    should_print = False
    temp_wait = timestamp + 10
    
    if message not in list(self.logs.keys()):
      self.logs[message] = temp_wait
      should_print = True   
    elif timestamp >= self.logs[message]:
      self.logs[message] = temp_wait
      should_print = True
    data = {
      'wait': self.wait,
      'timestamp': timestamp,
      'message': message,
      'should_print': should_print
    }
    self.result.append(data)
    
    print(should_print, self.logs)
    return should_print

if __name__ == '__main__':
  logger = Logger()
  data = [
    [1, 'foo'], [2, 'bar'], [3, 'foo'], 
    [8, 'bar'], [10, 'foo'], [11, 'foo']
  ]
  for d in data:
    l = logger.shouldPrintMessage(d[0], d[1])
    #print(dumps(vars(logger), indent=2))
