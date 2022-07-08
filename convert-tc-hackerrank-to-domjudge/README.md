
# convert-tc-hackerrank-to-domjudge

A python script to convert test cases from Hackerrank to DOMjudge format.

## How to use

- Download this script.
- Make sure to have the `input` and `output` folder in the script's directory.
- Run the script:
```
> python convert_tc_hackerrank_to_domjudge.py [start_tc_num] [end_tc_num]
```

## Example

Say that we have our test cases like this:
```
our_folder
L convert_tc_hackerrank_to_domjudge.py
L input
  L input0.txt
  L input1.txt
  L ...
  L input30.txt
L output
  L output0.txt
  L output1.txt
  L ...
  L output30.txt
```

Then in `our_folder`, run this:
```
> python convert_tc_hackerrank_to_domjudge.py 0 30
```

