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
  
  def _instantiate_csv(self, ftype, mode, fields=None):
    file_obj = open(self.file_dict[ftype], mode)
    r_flag = 'r' in mode
    w_flag = 'w' in mode

    if r_flag and w_flag:
      file_obj.close()
      raise ValueError('Choose Either Read or Write Mode')    

    csv_instance_func = DictWriter if w_flag else DictReader
    return csv_instance_func(file_obj, fieldnames=fields)

  def solve_test1(self):
    in_reader = self._instantiate_csv('input', 'r')
    st_reader = self._instantiate_csv('state', 'r')
    out_writer = self._instantiate_csv('output', 'w', in_reader.fieldnames) 
    st_dict = { st.values()[0] : st.values()[1] for st in st_reader }
    out_writer.writeheader()

    for curr_dict in in_reader:
      new_dict = { key : value for key, value in curr_dict.items() }
      new_dict['state'] = st_dict[new_dict['state']] 
      new_dict['bio'] = " ".join(new_dict['bio'].split()) 
      out_writer.writerow(new_dict)
  
def main():
  ans = Solution()
  ans.solve_test1()

if __name__ == "__main__":
  main()
