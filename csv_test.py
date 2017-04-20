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
  
  def create_csv_reader(self, filename):
    file_obj = open(filename, 'r')
    reader = csv.DictReader(file_obj)
    return reader

  def create_csv_writer(self, filename, fieldnames): # we could add **kwargs to make use of the csv writer settings 
    file_obj = open(self._out_filename, 'w')
    writer = csv.DictWriter(file_obj, fieldnames)  
    return writer
      
  
  def solve_test1(self):
    in_reader = self.create_csv_reader(self._in_filename)

    state_reader = self.create_csv_reader(self._state_filename)
    state_dict = dict([ state.values() for state in state_reader ])

    out_writer = self.create_csv_writer(self._out_filename, in_reader.fieldnames) 
    out_writer.writeheader()

    for curr_dict in in_reader:
      new_dict = {}
      for key in curr_dict.keys():
        if key == 'bio':
          new_dict['bio'] = " ".join(curr_dict['bio'].split()) #Space-delimited formatting of bio
        elif key == 'state':
          new_dict['state'] = state_dict[curr_dict['state']]
        else:
          new_dict[key] = curr_dict[key]
      out_writer.writerow(new_dict)
      #after this function is done, all file objects are destroyed
  
def main():
  ans = Solution()
  ans.solve_test1()



if __name__ == "__main__":
  main()
