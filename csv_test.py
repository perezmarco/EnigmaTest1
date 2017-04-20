import os
import csv
import sys

class Solution(object):

  def __init__(
      self,
      in_filename = 'test.csv',
      out_filename = 'solution.csv',
      state_filename = 'state_abbreviations.csv'):
      
    self.sol_dict = dict()
    self._in_filename = in_filename
    self._out_filename = out_filename
    self._state_filename = state_filename
    
  
  def create_dict(self):
    in_file = open(self._in_filename, 'r')
    state_file = open(self._state_filename, 'r')
    out_file = open(self._out_filename, 'w')
    in_reader = csv.DictReader(in_file)
    state_reader = csv.DictReader(state_file)
    out_writer = csv.DictWriter(out_file, in_reader.fieldnames)
    out_writer.writeheader()
    state_dict = {}
    for state in state_reader:
      state_tuple = state.values()
      state_dict[state_tuple[0]] = state_tuple[1]

    for curr_dict in in_reader:
      new_dict = {}
      for k in curr_dict.keys():
        if k == 'bio':
          new_dict[k] = " ".join(curr_dict[k].split())
        elif k == 'state':
          new_dict[k] = state_dict[curr_dict[k]]
        else:
          new_dict[k] = curr_dict[k]
      print new_dict.items()
      out_writer.writerow(new_dict)
    out_file.close()
    in_file.close()
  
def main():
  s = Solution()
  s.create_dict()



if __name__ == "__main__":
  main()
