import argparse
import string
import sys


# argparse function to handle user input
# Reference: https://docs.python.org/3.6/howto/argparse.html
# define a string to hold the usage error msg
def parse_arguments():
    usage_string = ("fw.py file")
    parser = argparse.ArgumentParser(usage=usage_string)

    parser.add_argument("file",
                        help="file containing firewall rules",
                        type=str)
    args = parser.parse_args()

    # # check that port is in a valid range
    # if args.port < 0 or args.port > 65535:
    #     parser.exit("usage: " + usage_string)
    return args


def main():
    args = parse_arguments()


if __name__ == '__main__':
    main()
