import os
import sys

def replace_clrf_with_lf(file_name):
  WINDOWS_LINE_ENDING = b'\r\n'
  UNIX_LINE_ENDING = b'\n'
  with open(file_name, 'rb') as open_file:
    content = open_file.read()
  content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
  with open(file_name, 'wb') as open_file:
    open_file.write(content)

start_num = -1
end_num = -1

if len(sys.argv) <= 2:
  print('Please provide start and end number of test cases (e.g. 1 40)')
  sys.exit()
if len(sys.argv) >= 3:
  start_num = int(sys.argv[1])
  end_num = int(sys.argv[2])

for i in range(start_num, end_num + 1):
  input_file = f'{i}.in'
  if os.path.isfile(input_file):
    replace_clrf_with_lf(input_file)
    print(f'{input_file} replaced.')
  else:
    print(f'{input_file} not found.')

  answer_file = f'{i}.ans'
  if os.path.isfile(answer_file):
    replace_clrf_with_lf(answer_file)
    print(f'{answer_file} replaced.')
  else:
    print(f'{answer_file} not found.')

print('Done.')
