from Generator.codeswapper import swap_code

import os
import unittest

class TestCodeSwapper(unittest.TestCase):

  def test_001(self):
    output_html = "<html><h1>Test!</h1>print ('Hello, world!')\n <br>"
    input_html = "<html><h1>Test!</h1>--codeswapper[test_codeswapper.html] <br>"
    swapped_html = swap_code(os.getcwd()+'/Tests', input_html)
    self.assertEqual(output_html, swapped_html)

if __name__ == "__main__":
  unittest.main()
