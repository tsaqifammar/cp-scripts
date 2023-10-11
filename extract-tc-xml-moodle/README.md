# Moodle Test Case Extractor

This script automates the extraction of test cases from Moodle's XML files and creates corresponding input files (with `.in` extension) and answer files (with `.ans` extension).
The generated files can seamlessly integrate with various programming platforms such as DOMjudge.

## Usage

1. Ensure Python is installed on your system, and install the required library [`xmltodict`](https://pypi.org/project/xmltodict/) using pip:
```bash
pip install xmltodict
```
2. Place both the script (`parse-tc-moodle.py`) and your Moodle XML file in the same directory.
3. Modify the `file_name` variable within the script to match the name of your XML file.
4. Run the script using the following command:
```bash
python parse-tc-moodle.py
```

## Example

Executing the script using the provided example Moodle XML file  (`question_exported_xml_example.xml`) will generate the following:
```
your_folder
L 0.in
L 0.ans
L 1.in
L 1.ans
...
L 13.in
L 13.ans
```
