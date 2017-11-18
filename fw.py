import argparse
import string
import sys

rules = [] # global list to hold a set of rules (dictionaries)

# returns True if line is valid rule, False otherwise
def validate_line(line):
    return True #TODO perform all error checking for the line here

# returns a ditionary containing the rule from the argument
def create_rule(line):
    rule = {}
    if (len(line) == 4):
        rule["direction"] = line[0]
        rule["action"] = line[1]
        rule["ip"] = line[2]
        rule["ports"] = line[3]
        rule["flag"] = None
    elif (len(line) == 5):
        rule["direction"] = line[0]
        rule["action"] = line[1]
        rule["ip"] = line[2]
        rule["ports"] = line[3]
        rule["flag"] = line[4]
    else:
        raise ValueError("Error: Invalid line")
    return rule

# read in the firewall rules from the config file
def read_config(filename):
    global rules
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.split()
            # check if the line contains a valid rule
            if validate_line(line):
                # create and add the rule to the rules list
                rules.append(create_rule(line))

def read_input_packets():
    print(rules)
    for line in sys.stdin:
        line = line.strip() # strip extra whitespace
        print(line)

# argparse function to handle user input
# Reference: https://docs.python.org/3.6/howto/argparse.html
# define a string to hold the usage error msg
def parse_arguments():
    usage_string = ("fw.py filename")
    parser = argparse.ArgumentParser(usage=usage_string)

    parser.add_argument("filename",
                        help="file containing firewall rules",
                        type=str)
    args = parser.parse_args()

    # if args.port < 0 or args.port > 65535:
    #     parser.exit("usage: " + usage_string)

    return args


def main():
    args = parse_arguments()
    read_config(args.filename) # read in the firewall rules
    read_input_packets()

if __name__ == '__main__':
    main()
