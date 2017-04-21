import os
from csv import DictReader, DictWriter
import sys

class Solution(object):

  def __init__(
      self,
      in_filename = 'test.csv',
      out_filename = 'solution.csv',
      state_filename = 'state_abbreviations.csv'):

    self.file_dict = { 'input' : in_filename,
                       'output': out_filename,
                       'state' : state_filename }
  
  def _create_csv_reader(self, filename):
    file_obj = open(self.file_dict[filename], 'r')
    reader = DictReader(file_obj)
    return reader

  # we could add **kwargs to make use of the csv writer settings 
  def _create_csv_writer(self, filename, fieldnames): 
    file_obj = open(self.file_dict[filename], 'w')
    writer = DictWriter(file_obj, fieldnames)  
    return writer

  def _instantiate_csv(self, ftype, mode, fields=None):
    file_obj = open(self.file_dict[ftype], mode)
    r_flag = 'r' in mode
    w_flag = 'w' in mode
    if r_flag and w_flag:
      file_obj.close()
      raise ValueError('Choose Either Read or Write Mode')    
    csv_instance = DictWriter if write_flag else DictReader
    return csv_instance(file_obj, fieldnames=fields)

  def date_formats(self, datestring):
    """
      %b/%B/%m/%-m %d/%-d %y/%Y
    """
    pass
      
  def solve_test1(self):
    in_reader = self._instantiate_csv('input', 'r')
    state_reader = self._instantiate_csv('state', 'r')
    out_writer = self._instantiate_csv('output', 'w', in_reader.fieldnames) 
    state_dict = {state.values()[0] : state.values()[1] for state in state_reader }
    out_writer.writeheader()

    for curr_dict in in_reader:
      new_dict = { key : value for key, value in curr_dict.items() }
      new_dict['state'] = state_dict[new_dict['state']] 
      new_dict['bio'] = " ".join(new_dict['bio'].split()) 
      out_writer.writerow(new_dict)
  
def main():
  ans = Solution()
  ans.solve_test1()

if __name__ == "__main__":
  main()
