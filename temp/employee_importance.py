#!usr/bin/env python3

from dataclasses import dataclass
from typing import Dict, List

def employee_importance(employees: List[int], id: int) -> int:
  store = {}
  
  employee_count = len(employees)
  for i in range(employee_count):
    store[employees[i][0]] = {'importance_value': employees[i][1],
                              'subordinates': employees[i][2]}
  
  importance = store[id]['importance_value']
  for subordinate_id in store[id]['subordinates']:
    importance += store[subordinate_id]['importance_value']
    
  print(store)
  return importance
        
if __name__ == '__main__':
  # uqique id, importance value, direct subordinates
  employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
  id = 1
  importance = employee_importance(employees, id)
  print(importance)
  
  employees = [[1,2,[2]], [2,3,[]]]
  id = 2
  importance = employee_importance(employees, id)
  print(importance)
