import xmltodict, json, os, sys

file_name = 'summation_function';

# Check if file exists
if not os.path.isfile(f'{file_name}.xml'):
  print("File not found.")
  sys.exit()

# Read xml text
with open(f"{file_name}.xml", "rb") as f:
  xml_text = f.read()

# Convert xml to dict
question_data = xmltodict.parse(xml_text)

# Get test cases
test_cases = question_data["quiz"]["question"]["testcases"]["testcase"]

def replace_crlf_with_lf(text: bytes):
  WINDOWS_LINE_ENDING = b'\r\n'
  UNIX_LINE_ENDING = b'\n'
  text.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

# Process test cases and export into .in and .ans files
for i in range(len(test_cases)):
  stdin = bytes(test_cases[i]["stdin"]["text"], encoding="utf-8")
  expected = bytes(test_cases[i]["expected"]["text"], encoding="utf-8")

  replace_crlf_with_lf(stdin)
  replace_crlf_with_lf(expected)

  with open(f"{i}.in", "wb") as input_file:
    input_file.write(stdin)
  with open(f"{i}.ans", "wb") as ans_file:
    ans_file.write(expected)
