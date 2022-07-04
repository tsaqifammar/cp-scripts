import os
import sys

n = 10
start_tc_num = 1

# Modifying `n` and `start_tc_num` if argument is given
if len(sys.argv) >= 2: n = int(sys.argv[1])
if len(sys.argv) >= 3: start_tc_num = int(sys.argv[2])

# Checking if all needed files exist
if not os.path.isfile('solution.cpp'):
  print('The file `solution.cpp` is not found')
  sys.exit()

if not os.path.isfile('gen.cpp'):
  print('The file `gen.cpp` is not found')
  sys.exit()

# Compiling gen.cpp and solution.cpp
print('Compiling gen, solution...')
os.system('g++ gen.cpp -std=c++14 -o gen')
os.system('g++ solution.cpp -std=c++14 -o solution')
print('Done compiling.')

def replace_clrf_with_lf(file_name):
  WINDOWS_LINE_ENDING = b'\r\n'
  UNIX_LINE_ENDING = b'\n'
  with open(file_name, 'rb') as open_file:
    content = open_file.read()
  content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
  with open(file_name, 'wb') as open_file:
    open_file.write(content)

# Start generating test cases
last_tc_num = start_tc_num + n - 1
for i in range(start_tc_num, last_tc_num + 1):
  print(f'Generating test case #{i}')
  os.system(f'gen > {i}.in')
  os.system(f'solution < {i}.in > {i}.ans')
  replace_clrf_with_lf(f'{i}.in')
  replace_clrf_with_lf(f'{i}.ans')

print('Done.')
