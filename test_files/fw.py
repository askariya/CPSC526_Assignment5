import argparse
import sys
import funcs

rules = [] # global list to hold a set of rules (dictionaries)

def print_error(message):
    print(message, file=sys.stderr)

# read in the firewall rules from the config file
def read_config(filename):
    global rules
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.split()
            # check if the line contains a valid rule
            rule, correct = funcs.create_rule(line)
            if correct:
                # create and add the rule to the rules list
                rules.append(rule)
            else:
                print_error("Rule Error")

# reads in the packets from std input
def read_input_packets():
    for line in sys.stdin:
        line = line.strip() # strip extra whitespace
        packet, correct = funcs.create_packet(line)
        # if the packet is invalid, skip
        if not correct:
            print_error("Packet Error")
            continue
        # print output
        print(funcs.validate_packet(rules, packet))

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
    return args


def main():
    args = parse_arguments()
    read_config(args.filename) # read in the firewall rules
    read_input_packets()

if __name__ == '__main__':
    main()
