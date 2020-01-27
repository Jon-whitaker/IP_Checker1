from pprint import *
from random import choice
import re, time, readline, ipaddress


free_ips = []
taken_ips = []
used_ip_set = set()


import ipaddress

def network_chk(prompt):
    while True:
        try:
           value = ipaddress.IPv4Network(str(input(prompt)))
        except ValueError as e:
            print("\n" + str(e) + "\n" + "\n" + "Now try typing it in properly you fat fingered spastic! "+"\n")  ### need a list of insults for a %s situation
            continue

        chk = input('You typed ' + str(value) + ' is that correct? (Y/N)')
        if chk.lower() not in ('y', 't', 'u'):
            continue
        else:
            break

    return value

adrs = network_chk(" What's the network address? i.e. (192.168.1.0/24) ")


for ip in ipaddress.IPv4Network(adrs):
    free_ips.append(str(ip))

def extract_ips(x):
    #search engine needed to find IPs
    return re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", x)


def source_file_IP_checker2(d):
    #using the search engine this method extracts the IP addresses from the source text file
    for line in d:
        for ip in extract_ips(line):
            if ip in free_ips:
                taken_ips.append(ip)
                free_ips.remove(ip)
    return (free_ips)
    return(taken_ips)

###################

def main():
    for file in sys.arg[1:]:
        f = open(file "rb")
        source_file_IP_checker2(f)
        f.close()

###################

# File runs, input is required at the moment in the form of what network range is being looked for, but I might want to change that, I'm not sure whether to have it run as:
    #c:\Users\J> python ip_c.py arg1 arg2 arg3 etc... <network address> or just   c:\Users\J> python ip_c.py arg1 arg2 arg3 then when it runs it asks you what network range you're looking for.
    # if i did the latter, I'd have to .. change the way address_chk works, and make source_file_IP_checker() take multiple args.
    # need to work out how to open each file I pass to source_file_IP_checker if I pass the names in the *args field.****

# path_check()
#source_file_IP_checker(f)
address_check(used_ip_set)
pprint("")
pprint(" IPs already in use: " + str(taken_ips))
time.sleep(1)
pprint("")
pprint(" All Free IP addresses: " + str(free_ips))
f.close()