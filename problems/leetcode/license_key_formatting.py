#!/usr/bin/env python3

def license_key_formatting(S: str, K: int) -> str:
    ''' 482. License Key Formatting
    https://leetcode.com/problems/license-key-formatting    
    '''
    
    # convert alpha chars to uppercase
    S = S.upper().replace('-', '')
    store = ''

    while True:
        # add the last K chars in S to the store
        store = '-' + S[-K:] + store
        # remove the K chars from S
        S = S[:-K]
        if len(S) <= 0:
            break
    return store[1:]

if __name__ =='__main__':
  fk = license_key_formatting("5f3Z-2e-9-w", 4)
  print(fk)
