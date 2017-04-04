import re

swap_pattern = "--codeswapper\[[A-Za-z0-9\._]+\]"
file_pattern = "\[[A-Za-z0-9\._]+\]"
folder_root = "../TestBlogContent/" # goes away too, but not yet

# this section is removed if operating against a Blog
with open("../TestBlogContent/myblog.html", "r") as file_in:
  core_blog = file_in.read()


def swap_code(html_in)
  ''' takes basic html blog and adds code section from pygment '''
  sections_to_swap = re.findall(swap_pattern, html_on)

  for section in sections_to_swap:
    # print ("code to swap! {}".format(section))
    file_match = re.search(file_pattern, section)
    file_to_swap = file_match.group()[1:-1]
    with open(folder_root+file_to_swap, "r") as new_content:
      new_html = new_content.read()
    html_out = core_blog.replace(section, new_html)

  return html_out
