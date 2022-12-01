#!/usr/bin/python3
# 100-print_tebahpla.py

for i in range(0, 26, 2):
    print("{:c}{:c}".format(122 - i, (122 - i - 1) - 32), end='')
