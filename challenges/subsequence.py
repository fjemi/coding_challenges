'''
Find longest word in dictionary that is a subsequence of a given string

https://techdevguide.withgoogle.com/resources/find-longest-word-in-dictionary-that-subsequence-of-given-string/#!
'''
# Library to get the maximum value from a dictionary
import operator

S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo", "abple"}
count = 0
ss_max = 0

# Function to find subsequences of a string
def subsequence(string, sub_string):
  s_bool = False
  sub_count = 0
  
  for s_index in range(0, len(string)):
    for ss_index in range(0, len(sub_string)):
      if sub_string[ss_index] == string[s_index]:
        sub_count += 1
        s_index += 1 # Increment the string counter in the outer for loop
        continue  # Move on to the next char in the substring if the char is found in the string
  
  # Add the subsquence to the list if count is greater than or equal to the length of the subsequence
  if sub_count >= len(sub_string):
    s_bool = True
  
  return s_bool
  
ss_len = 0
ss_current = []

# Create a list of substrings that are subsequences of S
for item in D:
  if subsequence(S, item) == True and len(item) >= ss_len:
    ss_current.append((item, len(item)))
    ss_len = len(item)
    count += 1

# Print the maximum lengthed substring from the list
print(ss_current)
print(max(ss_current))

