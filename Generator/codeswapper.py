import re

swap_pattern = "--codeswapper\[[A-Za-z0-9\._]+\]"
file_pattern = "\[[A-Za-z0-9\._]+\]"
folder_root = "../TestBlogContent/" # goes away too, but not yet

def swap_code(root_folder, html_in):
  ''' takes basic html blog and adds code section from pygment '''
  sections_to_swap = re.findall(swap_pattern, html_in)
  html_out = html_in
  for section in sections_to_swap:
    file_match = re.search(file_pattern, section)
    file_to_swap = file_match.group()[1:-1]
    with open(root_folder+"/"+file_to_swap, "r") as new_content:
      new_html = new_content.read()
    html_out = html_out.replace(section, new_html)

  return html_out
