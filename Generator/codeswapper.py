import re

swap_pattern = "--codeswapper\[[A-Za-z0-9\._]+\]"
#end_key = "]"

with open("../TestBlogContent/myblog.html", "r") as file_in:
  core_blog = file_in.read()

sections_to_swap = re.findall(swap_pattern, core_blog)
#print (sections_to_swap)


#first_swap = core_blog.find(swap_key)
#end_swap = core_blog[first_swap+len(swap_key):].find(end_key)

#print (first_swap, end_swap)

#section_to_swap = core_blog[first_swap:first_swap+len(swap_key)+end_swap+1]
#print (section_to_swap)

#if first_swap > -1:
#  print ("code to swap!")
#  file_to_swap = (core_blog[first_swap+len(swap_key):first_swap+len(swap_key)+end_swap])
#  print (file_to_swap)
#  with open(file_to_swap, "r") as new_content:
#    new_html = new_content.read()

##print (new_html)

##new_blog = core_blog.replace(section_to_swap, new_html)

##with open("new_blog.html", "w") as generated_blog:
##  generated_blog.write(new_blog)
