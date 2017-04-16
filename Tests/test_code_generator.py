from Generator.code_generator import generate_code_as_html

import os
import unittest


class TestCodeGenerator(unittest.TestCase):
  ''' tests code_generator.py '''

  def test_001(self):
    file_code_in = os.getcwd() + "/Tests/pygment_test.py"
    file_html_out = os.getcwd() + "/Tests/pygment_test_output.html"
    success = generate_code_as_html(file_code_in, file_html_out, test_status=True)
    with open(file_html_out, "r") as filein:
      output_html = filein.read()

    with open(os.getcwd()+"/Tests/pygment_test_actual.html","r") as filein:
      actual_html = filein.read()
    self.assertEqual(output_html, actual_html)


if __name__ == "__main__":
  unittest.main()
