from Generator.blog import Blog
from Generator.code_generator import generate_code_as_html

import os

code_extensions = ["py", "sh", "java", "js", "c", "rb", "rs", "cs", "cpp"]


if __name__ == "__main__":
  root_folder = os.getcwd() + "/BlogContent/"
  for dir in os.listdir(root_folder):
    if os.path.isdir(root_folder + dir):
      ''' menu will require another folder structure, later '''
      #print (root_folder + dir)
      #print (os.listdir(root_folder + dir))
      code_list = [code_file for code_file in os.listdir(root_folder + dir) if code_file.split(".")[-1] in code_extensions]
      all_code_to_convert = {root_folder + dir + "/" + code_file: root_folder + dir + "/" + code_file.split(".")[0] + ".html" for code_file in code_list}
      print (code_list)
      print (all_code_to_convert)
      all_code_as_html = []
      for code_to_convert, code_as_html in all_code_to_convert.items():
        success = generate_code_as_html(code_to_convert, code_as_html)
        if success:
          all_code_as_html.append(code_as_html)
      print (all_code_as_html)
      title = dir
      menu = "Programming"
      markdown = dir + ".md"
      next_blog = Blog(title, menu, root_folder + dir +"/", markdown, all_code_as_html)
      next_blog.generate_blog()
