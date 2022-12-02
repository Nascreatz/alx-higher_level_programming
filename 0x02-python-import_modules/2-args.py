#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    index = 1
    if argv_count is 0:
        print("{:d} arguments.".format(argv_count))
    elif argv_count is 1:
        print("{:d} argument:".format(argv_count))
        print("{:d}: {:s}".format(index, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_count))
        while index <= argv_count:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
