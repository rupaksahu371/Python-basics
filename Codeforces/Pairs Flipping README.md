# Pairs Flipping - Codeforces Problem Solution

## Problem Description

This program solves the Codeforces problem "Pairs Flipping" (also known as "Flipping Game" or similar variants).

Given a binary string of length `n`, you need to make the string palindromic by performing operations. In each operation, you choose an index `l` and flip (change '0' to '1' or '1' to '0') the characters at positions `l` and `n-l+1` (symmetric pairs from both ends).

The goal is to determine which indices to flip to make the string palindromic.

## How It Works

1. **Input Format**:
   - First line: `t` - number of test cases
   - For each test case:
     - First line: `n` - length of the binary string
     - Second line: `s` - the binary string (containing only '0' and '1')

2. **Algorithm**:
   - For each test case, iterate from the outside towards the center
   - For each pair of symmetric positions (left and right):
     - If characters are different: flip both characters and record the left index
     - If characters are already equal: do nothing (no operation needed)
   - Output the list of indices used for flipping

3. **Output**:
   - For each test case, print a line containing the indices (0-based) used for flipping, separated by spaces

## Example

**Input:**
```
3
4
0110
2
01
6
100110
```

**Output:**
```
 (empty line)
0
0 1 2
```

**Explanation:**
For input "0110" of length 4:
- x=1: left=0, right=3 → s[0]='0', s[3]='0' → equal → no flip
- x=2: left=1, right=2 → s[1]='1', s[2]='1' → equal → no flip
- Output: "" (empty line)

For "01" of length 2:
- x=1: left=0, right=1 → s[0]='0', s[1]='1' → different → flip both, ans=[0]
- Output: "0"

For "100110" of length 6:
- x=1: left=0, right=5 → s[0]='1', s[5]='0' → different → flip both, ans=[0], s becomes "000110"
- x=2: left=1, right=4 → s[1]='0', s[4]='1' → different → flip both, ans=[0,1], s becomes "001010"
- x=3: left=2, right=3 → s[2]='0', s[3]='1' → different → flip both, ans=[0,1,2], s becomes "000000"
- Output: "0 1 2"

## Running the Program

```
bash
python "Python coding/Pairs Flipping.py"
```

Then enter the input as shown in the example above.

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Files

- `Pairs Flipping.py` - Main program
- `Pairs Flipping README.md` - This documentation
