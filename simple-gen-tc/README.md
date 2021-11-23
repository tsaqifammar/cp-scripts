# Simple Test Case Generator

## What it is
A simple batch script to generate multiple test cases in a matter of seconds.

## Note

* This only works on Windows.
* I've only tested this for problemsetting on Hackerrank. You may need to slightly modify this if you're conducting contests on other platforms.

## How to use
1. You have to prepare 2 other programs along with this script. Those are, the randomized input generator (`gen.cpp`), and the solution (`solution.cpp`).
2. Have them all in the same folder/directory.
3. Open your command prompt there.
4. Do one of the following depending on your needs:
	* Generate 10 test cases (input and output), starting from test case #1
	```
	> gen_tc
	```

	* Generate `n` test cases (input and output), starting from test case #1
	```
	> gen_tc [n]
	```

	* Generate `n` test cases (input and output), starting from test case #`k`
	```
	> gen_tc [n] [k]
	```

## Example of Usage
Generate 15 test cases, starting from test case #6 :
```
> gen_tc 15 6
```
This will generate 15 input and output files (30 in total) like this :
```
your_folder
L input6.txt
L output6.txt
L input7.txt
L output7.txt
  ...
L input20.txt
L output20.txt
```


