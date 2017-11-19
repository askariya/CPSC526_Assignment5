import argparse
import string
import sys

rules = [] # global list to hold a set of rules (dictionaries)

# returns True if line is valid rule, False otherwise
def check_rule(line):
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
            if check_rule(line):
                # create and add the rule to the rules list
                rules.append(create_rule(line))

# creates and returns a dictionary containing a packet
def create_packet(line):
    packet = {}
    line = line.split()
    if len(line) != 4:
        return None, False

    packet["direction"] = line[0]
    packet["ip"] = line[1]
    packet["port"] = line[2]
    packet["flag"] = line[3]

    # ERROR CHECKING
    # direction
    if packet["direction"] not in ("in", "out"):
        return None, False

    # IP
    ip = packet["ip"].split(".")
    if len(ip) != 4:
        return None, False
    try:
        for num in ip:
            if int(num) not in range (0, 256):
                return None, False
    except:
        return None, False

    # port
    try:
        if int(packet["port"]) not in range(0, 65536):
            return None, False
    except:
        return None, False

    # flag
    if packet["flag"] not in ("0", "1"):
        return None, False

    # successful packet -- no errors
    return packet, True

# checks the packet against the rules
def validate_packet(packet):
    for rule in rules:
        # check direction
        if packet["direction"] != rule["direction"]:
            continue
        # check IP
        # check port
        # check flag

def check_IP():
    pass # TODO Compare the IPs here

# reads in the packets from std input
def read_input_packets():
    for line in sys.stdin:
        line = line.strip() # strip extra whitespace
        packet, valid = create_packet(line)
        # if the packet is invalid, skip
        if not valid:
            # print("Packet Error")
            continue
        validate_packet(packet)
        # print(packet)

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
