######## HOW TO USE ########
#
#  src ips
#  1.1.1.1
#  2.2.2.2
#  ---
#  dst ips
#  3.3.3.3
#  4.4.4.4
#  ---
#  tcp ports
#  80
#  443
#
############################


import re
import struct
import pyperclip
import datetime as dt
from pprint import pprint
from socket import inet_aton, inet_ntoa


def ip2long(ip):
    packed = inet_aton(ip)
    lng = struct.unpack("!L", packed)[0]
    return lng


def acl_unfold(protocol='tcp'):
    new_list = []
    print('\nSOURCE IP SORTED:')
    for i in re.split(r'-+', pyperclip.paste()):
        new_list.append(i.strip().split())
    n = 0
    sorted_list = []
    full_access_list = []
    for x in sorted(new_list[0], key=lambda x: ip2long(x)):
        for y in sorted(new_list[1], key=lambda z: ip2long(z)):
            for z in new_list[2]:
                print(f'access-list test extended permit {protocol} host {x} host {y} eq {z}')
                sorted_list.append(f'access-list test extended permit {protocol} host {x} host {y} eq {z}')
                full_access_list.append(f'access-list test extended permit {protocol} host {x} host {y}')
                n += 1
    
    print(f'\nDESTINATION IP SORTED(number of entries - {n}):')
    list_of_lists = []
    for line in sorted_list:
        list_of_lists.append(line.split())
    for i in sorted(list_of_lists, key=lambda x: ip2long(x[8])): # sorting IPs by: index 6 for src, 8 for dst
        print(' '.join(i))

    print(f'\nFULL ACCESS ACL(number of entries - {len(set(full_access_list))}):')
    for line in sorted(set(full_access_list), key=lambda x: ip2long(x.split()[8])): # sorting IPs by: index 6 for src, 8 for dst
        print(line)


def acl_obj_groups():
    new_list = []
    for i in re.split(r'-+', pyperclip.paste()):
        new_list.append(i.strip().split())
    
    print()
    src = f'object-group network SRC-SRV-{current_date}'
    print(src)
    for x in sorted(new_list[0], key=lambda x: ip2long(x)):
        print(f'network-object host {x}')

    print()
    dst = f'object-group network DST-SRV-{current_date}'
    print(dst)
    for x in sorted(new_list[1], key=lambda x: ip2long(x)):
        print(f'network-object host {x}')

    print()
    ports = f'object-group service TCP-{current_date} tcp'
    print(ports)
    for x in sorted(new_list[2], key=int):
        print(f'port-object eq {x}')

    print()
    print(f'access-list test extended permit tcp object-group SRC-SRV-{current_date}'
          f' object-group DST-SRV-{current_date} object-group TCP-{current_date}')


choice = input('\n1 for standard_acl, 2 for obj_groups, 3 for standard_acl_udp: ')
current_date = dt.datetime.now().strftime('%H%M%d%m%y')

if int(choice) == 1:
    acl_unfold()
elif int(choice) == 2:
    acl_obj_groups()
elif int(choice) == 3:
    acl_unfold(protocol='udp')
else:
    print('wrong choice')
