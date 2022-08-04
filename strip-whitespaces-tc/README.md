# Strip trailing/leading whitespaces of Test Cases

This script will strip trailing/leading whitespaces in files with extensions `.in` and `.ans`.

Warning: This script will remove empty lines, don't use this script if you have empty lines in your test cases (especially `.ans`).

# How to use

To run, have your script in your test case folder like this:

```
your_folder
L strip.py
L 1easy.in
L 1easy.ans
L 2easy.in
L 2easy.ans
L 1hard.in
L 1hard.ans
```

Run the script:
```
> python strip.py
```
