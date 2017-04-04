import markdown2


class Blog:
  ''' This is the basic blog object.  Creating these will eventually become blog postings '''

  def __init__(self, title, menu, markdown, code_list=[]):
    ''' nothing for now '''
    self.title = title
    self.menu = menu # this will hold the menu to return to
    self.markdown = markdown # will hold reference to local markdown file
    self.code_list = code_list # will hold list of code files to swap
    self.url = 'http://www.somesite.com/blog/{}.html'.format(self.title)

  def build_blog(self):
    ''' this will build and return html from markdown '''
    with open(self.markdown, "r") as file_to_read:
      data = file_to_read.read()
    html = markdown2.markdown(data, extras["footnotes"])
    return html

  def swap_code(self):
    ''' this will swap out html with pygment code if necessary '''
    pass
