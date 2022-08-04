# ! not safe for tcs with possible empty lines

import os

def strip_whitespaces(file_name):
  with open(file_name, 'r') as f:
    lines = f.readlines()
  strippedLines = []
  for line in lines:
    stripped = line.strip()
    if (len(stripped) != 0):
      strippedLines.append(stripped + '\n')
  with open(file_name, 'w') as f:
    f.writelines(strippedLines)

def replace_crlf_with_lf(file_name):
  WINDOWS_LINE_ENDING = b'\r\n'
  UNIX_LINE_ENDING = b'\n'
  with open(file_name, 'rb') as open_file:
    content = open_file.read()
  content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
  with open(file_name, 'wb') as open_file:
    open_file.write(content)

path = '.'
files_to_replace = [f for f in os.listdir(path) if f.endswith('.in') or f.endswith('.ans')]

for f in files_to_replace:
  full_path = os.path.join(os.getcwd(), f)
  print(f'Found {f}, removing trailing whitespaces...')
  strip_whitespaces(full_path)
  replace_crlf_with_lf(full_path)

print('Done')
