

class Blog:
  ''' This is the basic blog object.  Creating these will eventually become blog postings '''

  def __init__(self, title, menu, markdown):
    ''' nothing for now '''
    self.title = title
    self.menu = menu # this will hold the menu to return to
    self.markdown = markdown # will hold reference to local markdown file
    self.url = 'http://www.somesite.com/blog/{}.html'.format(self.title)

  def build_blog(self):
    ''' this will build and return html from markdown '''
    pass

  def swap_code(self):
    ''' this will swap out html with pygment code if necessary '''
    pass
