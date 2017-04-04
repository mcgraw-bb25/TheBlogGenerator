import re

swap_pattern = "--codeswapper\[[A-Za-z0-9\._]+\]"
file_pattern = "\[[A-Za-z0-9\._]+\]"
folder_root = "../TestBlogContent/"

# this section is removed if operating against a Blog
with open("../TestBlogContent/myblog.html", "r") as file_in:
  core_blog = file_in.read()

sections_to_swap = re.findall(swap_pattern, core_blog)

for section in sections_to_swap:
  print ("code to swap! {}".format(section))
  file_match = re.search(file_pattern, section)
  file_to_swap = file_match.group()[1:-1]
  with open(folder_root+file_to_swap, "r") as new_content:
    new_html = new_content.read()
  new_blog = core_blog.replace(section, new_html)

# no need to write to disk
with open("{}new_blog.html".format(folder_root), "w") as generated_blog:
  generated_blog.write(new_blog)
