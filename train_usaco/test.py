"""
ID: krishna91
LANG: PYTHON3
TASK: test
"""

with open("test.in", "r") as fin:
    line1 = fin.readline().strip().split(" ")
    x = int(line1[0]); y = int(line1[1])

with open("test.out", "w") as fout:
    fout.write(str(x+y) + '\n')