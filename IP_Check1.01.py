#! /usr/bin/python
from pprint import *
import ipaddress
import fileinput
free_ips = set()
taken_ips = set()

###################

def network_chk(prompt):
    while True:
        try:
           value = ipaddress.IPv4Network(str(input(prompt)))
        except ValueError as e:
            print("\n" + str(e) + "\n" + "\n" + "Now try typing it in properly you fat fingered spastic! "+"\n")  # need a list of insults for a %s situation
            continue
        chk = input('You typed ' + str(value) + ' is that correct? (Y/N)')
        if chk.lower() not in ('y', 't', 'u'):
            continue
        else:
            break
    return value

adrs = network_chk(" What's the network address? i.e. (192.168.1.0/24) ")


for ip in ipaddress.IPv4Network(adrs):
    free_ips.add(str(ip))

###################

for ip in free_ips:
    for line in fileinput.input():
        line1 = line.split()
        if ip in line1:
            taken_ips.add(ip)

for ip in taken_ips:
    if ip in free_ips:
        free_ips.remove(ip)
pprint("")
pprint("")
pprint("")
pprint("You can't use any of these IP addresses :")
pprint("")
pprint(str(sorted(taken_ips)))
pprint("")
pprint("")
pprint("But you can use any of these IP addresses  :")
pprint("")
pprint(str(sorted(free_ips)))