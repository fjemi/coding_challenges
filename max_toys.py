#!usr/bin/env python3


from typing import List


def model(prices: List[int], k: int):
  store = {}
  prices.sort()

  for i in range(len(prices)):
    if prices[i] > k:
      break

    if i not in store.keys() and prices[i] < k:
      store[i] = [prices[i]]

    #if i == len(prices) - 1 or prices[i] > k:
      #store[i] = len(store[i])
      #break

    for j in range(i + 1, len(prices)):
      if prices[j] > k:
        break

      if sum(store[i]) + prices[j] <= k:
        store[i].append(prices[j])
      else:
        break
    print(store)
    store[i] = len(store[i])    
  return max(store.values())


if __name__ == '__main__':
  inputs = [
    {'prices': [1,2,3,4], 'k': 7},
    {'prices': [1,12,5,111,200,1000,10], 'k': 50}
  ]
  for input in inputs:
    m = model(input['prices'], input['k'])
    print(m)