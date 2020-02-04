from netaddr import *
from pprint import *
from random import choice
from os.path import expanduser
import re, time, readline, rlcompleter, os

free_ips = []
taken_ips = []
used_ip_set = set()

config = input(
    " please copy/paste the name (including .txt) and file path of the file you wish to check. "
       "Hint: put it in the same location as this checker, then you can just enter the filename  ")

config_path_check = input(
    "is the following filename and path correct? " + config + " ")

adrs = input(
       " Using an IPv4 format, please enter the base NETWORK address of the subnet you're checking, including the CIDR notation, i.e. (192.168.1.0/24) ")

address_chk = input(
    " Y/N, is the following address & subnet mask correct? " + adrs + "  ") # what if they answer with anything other than y or n?

for ip in IPNetwork(adrs).iter_hosts():
    free_ips.append(str(ip))

f = open(config, buffering=1)

###################


def extract_ips(x):
    #search engine needed to find IPs
    return re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", x)

def source_file_IP_checker(d):
    #using the search engine this method extracts the IP addresses from the source text file
    for line in d:
        for ip in extract_ips(line):
            if ip not in used_ip_set:
                used_ip_set.add(str(ip))
    return(used_ip_set)

###################


def address_check(x):
    #compares the source text file IP address list and the search parameter.
    for ip in x:
        if ip in free_ips:
            taken_ips.append(ip)
            free_ips.remove(ip)
    return(free_ips)
    return(taken_ips)

###################


###################

ran1 = choice(loading_messages)


# path_check()
source_file_IP_checker(f)
address_check(used_ip_set)
print(ran1)
time.sleep(10)
pprint("")
pprint(" IPs already in use: " + str(taken_ips))
time.sleep(1)
pprint("")
pprint(" All Free IP addresses: " + str(free_ips))
f.close()
