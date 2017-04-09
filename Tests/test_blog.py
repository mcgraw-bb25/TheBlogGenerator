from Generator.blog import Blog

import os
import unittest


class TestBlog(unittest.TestCase):
  ''' Testing for blog.py '''

  def test_001(self):
    test_blog = Blog("Test Blog!", "No Menu", os.getcwd()+"/Tests/", "test_blog.md")
    success = test_blog.generate_blog()
    output_html = "<h1>Test</h1>\n\n<p>Hello, world!</p>\n"
    with open(test_blog.blog_root_folder+"test_blog.html", "r") as file_in:
      test_html = file_in.read()
    self.assertEqual(output_html, test_html)


if __name__ == "__main__":
  unittest.main()
