from codeswapper import swap_code

import markdown2
import pdb

root_url = "http://www.somesite.com/" # config this later


class Blog:
  ''' This is the basic blog object.  Creating these will eventually become blog postings '''

  def __init__(self, title, menu, markdown, code_list=[]):
    ''' nothing for now '''
    self.title = title
    self.menu = menu # this will hold the menu to return to
    self.markdown = markdown # will hold reference to local markdown file
    self.code_list = code_list # will hold list of code files to swap
    self.url = '{}blog/{}.html'.format(root_url, self.title)

  def build_blog(self):
    ''' this will build and return html from markdown '''
    with open(self.markdown, "r") as file_to_read:
      data = file_to_read.read()
    html = markdown2.markdown(data, extras=["footnotes"])
    #print (html)
    return html

  def add_code_snippets(self):
    ''' this will swap out html with pygment code if necessary '''
    html_in = self.build_blog()
    html_out = swap_code(html_in)
    return html_out

  def generate_blog(self):
    ''' builds the blog '''
    #import pdb; pdb.set_trace()
    success = False
    try:
      html_out = self.add_code_snippets()
      with open(self.markdown.replace(".md", ".html"), "w") as file_to_write:
        file_to_write.write(html_out)
      success = True
    except:
      pass
    return success


if __name__ == "__main__":
  myblog = Blog("My Blog", "Programming", "../TestBlogContent/myblog.md", ["../TestBlogContent/test_file.html"])
  success = myblog.generate_blog()
