######## HOW TO USE ########
#
#  src ip    dst ip    port number
#  1.1.1.1   2.2.2.2   80,443
#  1.1.1.1   2.2.2.2   80, 443
#
##############################

import re
import struct
import pyperclip
from pprint import pprint
from socket import inet_aton, inet_ntoa


def ip2long(ip):
    packed = inet_aton(ip)
    lng = struct.unpack("!L", packed)[0]
    return lng


new_list = []
print()
for line in pyperclip.paste().splitlines():
    split_acl = re.split(r'\s+|,\s*', line.strip())
    new_list.append(split_acl)
n = 0; final_list = []
for ace in new_list:
    for i in range(2, len(ace)): # starting index for TCP/UDP ports
        final_list.append(f'access-list dmz extended permit tcp host {ace[0]} host {ace[1]} eq {ace[i]}')
        print(f'access-list dmz extended permit tcp host {ace[0]} host {ace[1]} eq {ace[i]}')
        n += 1
print('\nNumber of lines:', n)

list_of_lists = []
for line in final_list:
    list_of_lists.append(line.split())

for i in sorted(list_of_lists, key=lambda x: ip2long(x[8])): # sorting IPs by: index 6 for src, 8 for dst
    print(' '.join(i))
