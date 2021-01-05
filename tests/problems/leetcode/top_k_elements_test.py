from get_problems_dir import get_problems_dir
PROBLEMS_DIR = get_problems_dir()

from top_k_elements import top_k_elements

def test_top_k_elements():
  '''
  '''
  
  test_cases = [
    {'nums': [1,1,1,2,2,3], 'k': 2, 'result': [1,2]},
    {'nums': [1], 'k': 1, 'result': [1]}
  ]

  for test in test_cases:
    TKE = top_k_elements(test['nums'], test['k'])
    assert TKE == test['result']
  