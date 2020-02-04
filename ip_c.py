from pprint import *
import re, ipaddress, sys
import fileinput



free_ips = []
taken_ips = []
used_ip_set = set()

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
    free_ips.append(str(ip))

###################

def extract_ips(x):
    #search engine needed to find IPs
    return re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", x)


def source_file_ip_checker(d):
    #using the search engine this method extracts the IP addresses from the source text file
    for line in d:
        for ip in extract_ips(line):
            if ip not in used_ip_set:
                used_ip_set.add(str(ip))
    return used_ip_set

###################


def address_check(x):
    #compares the source text file IP address list and the search parameter.
    for ip in x:
        if ip in free_ips:
            taken_ips.append(ip)
            free_ips.remove(ip)
        return free_ips
    return taken_ips

# def source_file_IP_checker2(d):
#     #using the search engine this method extracts the IP addresses from the source text file
#     for line in d:
#         for ip in extract_ips(line):
#             if ip in free_ips:
#                 taken_ips.append(ip)
#                 free_ips.remove(ip)
#     return (free_ips)
#     return(taken_ips)

###################
#
# def main():
# for file in sys.argv[1:]:
#     with open(file, "rb") as f:
#         source_file_ip_checker(f)

def main():
    for line in fileinput.input():
        used_ip_set.add(str(extract_ips(line)))


###################

# main()
# path_check()
source_file_ip_checker(f)
address_check(used_ip_set)
pprint("")
pprint(" IPs already in use: ")
pprint(str(taken_ips))
pprint("")
pprint(" All Free IP addresses: ")
pprint(str(free_ips))
f.close()
