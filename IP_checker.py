from netaddr import *
from pprint import *
from random import choice
from os.path import expanduser
import re, time, readline, rlcompleter, os

home = os.path.expanduser("~")
os.chdir(home)
# tab completion
readline.parse_and_bind('tab: complete')

loading_messages = [
    "humorous message loading, Please wait... ",
    """Please wait Testing RAM..............OK
       Testing CPU..............OK
       Testing Primary Disk.....OK
       Testing Patience.......""",

    "Please wait loading BSOD",
    "Error... fat finger syndrome detected",
    "Please wait we're having a meltdown...",
    "Please wait loose monkey found",
    "Please wait pregnant pixels incoming",
    "Please wait.... we encountered an error, I think... Barry, did we encounter an error?...",
    "hang on a second, who's sour cream is this on my screen?.. wait a minute, that's not sour cream!",
    "Please wait we found a leak in the flux capacitor",
    "Please wait not enough things to engage stuff",
    "Please wait incoming Jehovah's witnesses, run away!!",
    "Please wait while I fart in your general direction",
    "Please wait while we generate a random error message..",
    "Please wait, keyboard not responding, press any key to continue",
    "Please wait deleting the contents of C:/ press any key to continue..",
    "Please press OK to continue...",
    "You shouldn't be looking at this, please wait while we call your parents for permission..",
    "Aaaarrgghh, what are you doing here?... you shouldn't be here this early!",
    "Please wait while we attempt to locate your life.exe file... could take a while, better go get a coffee!",
    "Please come back later, we've been at it all day so far..",
    "Internal Error, too much bacon for a windows found.",
    "Tip of the day: your tips file is missing...",
    "Error, pornhub.exe says you've visited waaaayyy too much.. ",
    "Please wait while we recycle the recycle bin 1%....",
    "An error has occurred while creating an error, please come back later for a new error.. ",
    "Please wait while we prefab the sprout",
    "Please wait while we look at cat pictures",
    "Catastrophic failure detected: life.exe not located, press ok to continue.. ",
    "Please wait while we find someone who cares... ",
    "Unknown hard problem found: press F1 to erase hard drive, F2 to restart, F3 to error",
    "Please wait while we register your copy of windows",
    "Please wait, deleting file:best_mum_pics.zip, press F1 to load new file, F2 to quit",
    "You seem to be having a problem, would you like an adult to help you? (Y/N)",
    "Please wait while we look for a problem...",
    "Please wait while send your answer to the printer.",
    "User Error, replace user..",
    "Error, no error occurred, please replace error",
    "Please wait, all the relevant elves are on a break!",
    "Loading... for a quick IQ test press Alt+F4 now!",
    "Please wait loading spoon!",
    "Please wait loading cake...",
    "Error the cake is a lie..",
    "Please wait measuring cable length needed to fetch your data.... One inch..... Two inches.... ",
    "Please wait while the loading gods contemplate your fate",
    "Results found!.. please enter the square root of 9468351968749684 to continue",
    "results compiled, in order to recieve your results, please send £1000 in untraceable bills to... ",
    "Please wait, we're working on it.. so how are you?",
    "Please shut up, we're trying to think here!",
    "Please wait while we cache the internet",
    "Please wait quantum singularity loading",
    "Please wait time loop loading... please wait time loop loading... please wait, time loop loading...",
    "  Hic... I'm..   hic... a bit    hic.. drunk! haha...  canyougetme   hic.... a a a a...  sorrywhatwasIsaying?",
    "Please wait internet brokend",
    "Loading the loading messages..",
    "Please wait rewinding the tape..",
    "Please wait while we bring Skynet online.",
    "Please wait while we delete the hard drive",
    "Please wait, there's Klingons on the starboard bow",
    "Please wait while we calculate the meaning of life... 42.. huh, who'd have guessed!"
    ]

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
