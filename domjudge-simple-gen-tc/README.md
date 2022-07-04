# Simple Test Case Generator

## What it is
A simple python script to generate multiple test cases in a matter of seconds following the DOMjudge test case format.

## How to use
1. You have to prepare 2 other programs along with the script (`gen_tc.py`). Those are, the randomized input generator (`gen.cpp`), and the solution (`solution.cpp`). See the `example` folder for more details.
2. Have them all in the same folder/directory.
3. Open your command prompt there.
4. Do one of the following depending on your needs:
	* Generate 10 test cases (input and output), starting from test case #1
	```
	> python gen_tc.py
	```

	* Generate `n` test cases (input and output), starting from test case #1
	```
	> python gen_tc.py [n]
	```

	* Generate `n` test cases (input and output), starting from test case #`k`
	```
	> python gen_tc.py [n] [k]
	```

## Example of Usage

Generate 15 test cases, starting from test case #6 :

```
> python gen_tc.py 15 6
```

This will generate 15 input and output files (30 in total) like this :

```
your_folder
L 6.in
L 6.ans
L 7.in
L 7.ans
  ...
L 20.in
L 20.ans
```


