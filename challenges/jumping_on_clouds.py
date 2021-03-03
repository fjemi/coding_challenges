#!usr/bin/env python3

from typing import List

def jumping_on_clouds(c: List[int]) -> int:
  # set indices for cumulus clouds
  cumulus_clouds = []
  for i in range(len(c)):
    if c[i] != 1:
      cumulus_clouds.append(i)

  # count cloud jumps
  current = cumulus_clouds[0]
  jumps = 0
  for i in range(1, len(cumulus_clouds)):
    if (current + 2) in cumulus_clouds:
      current = current + 2
    else:
      current = current + 1
    jumps += 1

    if current == cumulus_clouds[-1]:
      break

  return jumps

if __name__ == '__main__':
  joc = jumping_on_clouds([0,1,0,0,0,1,0])
  print(joc)