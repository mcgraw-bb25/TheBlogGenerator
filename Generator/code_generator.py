import subprocess


def generate_code_as_html(file_code_in, file_html_out):
  ''' takes in a file and generates code as html '''
  success = False
  try:
    subprocess.run(["pygmentize", "-o", file_html_out, file_code_in], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    success = True
  except Exception as e:
    print ("generate_code_as_html() failed: {}".format(e))

  return success


if __name__ == "__main__":
  pass
