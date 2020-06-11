'''
You are given a input string N.
The task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

1) Number can start with +, - or . symbol.
For example:
+4.50
-1.0
.5
-.7
+.4
2) Number must contain at least 1 decimal value.
For example:
12.0  
3) Number must have exactly one . symbol.
4) Number must not give any exceptions when converted using float(N).
'''

import re

test_cases = int(input())
for i in range(test_cases):
    test_float = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', test_float)))
