@echo off

if [%1]==[] (set /A n = 10) else (set /A n = %1)
if [%2]==[] (set /A startTcNum = 1) else (set /A startTcNum = %2)

echo Compiling gen, solution...

g++ -std=c++14 gen.cpp -o gen
g++ -std=c++14 solution.cpp -o solution

echo Done compiling.

set /A endLoop = %startTcNum%+%n%-1
for /l %%x in (%startTcNum%, 1, %endLoop%) do (
    echo Generating test case #%%x
    gen > input%%x.txt
    solution < input%%x.txt > output%%x.txt
)
