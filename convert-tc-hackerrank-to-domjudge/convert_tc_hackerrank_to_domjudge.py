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

if not os.path.isdir('input') or not os.path.isdir('output'):
  print('Current directory must have 2 folders: input, output')
  sys.exit()

if len(sys.argv) <= 2:
  print('Please provide start and end number of tcs (e.g. 1 40)')
  sys.exit()
if len(sys.argv) >= 3:
  start_num = int(sys.argv[1])
  end_num = int(sys.argv[2])

for i in range(start_num, end_num + 1):
  input_path = os.path.join(os.getcwd(), 'input', f'input{i}.txt')
  output_path = os.path.join(os.getcwd(), 'output', f'output{i}.txt')

  # input
  if os.path.isfile(input_path):
    print(f'Generating {i}.in')
    os.system(f'powershell cp ./input/input{i}.txt {i}.in')
    replace_clrf_with_lf(f'{i}.in')
  else:
    print(f'input{i}.txt not found.')

  # output
  if os.path.isfile(output_path):
    print(f'Generating {i}.ans')
    os.system(f'powershell cp ./output/output{i}.txt {i}.ans')
    replace_clrf_with_lf(f'{i}.ans')
  else:
    print(f'output{i}.txt not found.')

print('Done.')
