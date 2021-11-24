# Stress Test Script for Competitive Programming

*Note: This only works on Windows.*

## How to use
1. You have to prepare 3 other programs along with this script. Those are, your original solution (`solution.cpp`), the bruteforce/correct solution (`brute.cpp`), and the randomized input generator (`gen.cpp`).
2. Have them all in the same directory.
3. Open your command prompt there.
4. Do one of the following depending on your needs:
   * Compile the 3 programs and stress test the solution on 100 randomized test cases:
   ```
   > stress
   ```
   
   * Compile the 3 programs and stress test the solution on `n` randomized test cases:
   ```
   > stress [n]
   ```

   * Stress test the solution on `n` randomized test cases without compiling the 3 programs:
   ```
   > stress [n] 0
   ```

## Video Guide + Demo

Link: https://youtu.be/qtJC0DONFXw