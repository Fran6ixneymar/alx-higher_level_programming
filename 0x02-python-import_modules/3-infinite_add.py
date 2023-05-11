#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    summation = 0
    for fig in range(len(sys.argv) - 1):
        summation += int(sys.argv[fig + 1])
    print("{}".format(summation))
