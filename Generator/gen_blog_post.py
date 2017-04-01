import markdown2

with open("myblog.md", "r") as readin:
  data = readin.read()

html = markdown2.markdown(data, extras=["footnotes"])

with open("myblog.html", "w") as writeout:
  writeout.write(html)
