```The script transforms the following IP template:

10.135.59.78
10.135.58.151
---
10.110.225.4
10.110.222.4
---
22
1521

into valid Cisco ASA ACLs:

access-list test extended permit tcp host 10.135.59.78 host 10.110.225.4 eq 22
access-list test extended permit tcp host 10.135.59.78 host 10.110.225.4 eq 1521
access-list test extended permit tcp host 10.135.59.78 host 10.110.222.4 eq 22
access-list test extended permit tcp host 10.135.59.78 host 10.110.222.4 eq 1521
access-list test extended permit tcp host 10.135.58.151 host 10.110.225.4 eq 22
access-list test extended permit tcp host 10.135.58.151 host 10.110.225.4 eq 1521
access-list test extended permit tcp host 10.135.58.151 host 10.110.222.4 eq 22
access-list test extended permit tcp host 10.135.58.151 host 10.110.222.4 eq 1521

or by using object-groups:

object-group network SRC-SRV-1155061119
network-object host 10.135.59.78
network-object host 10.135.58.151

object-group network DST-SRV-1155061119
network-object host 10.110.225.4
network-object host 10.110.222.4

object-group service TCP-1155061119 tcp
port-object eq 22
port-object eq 1521

access-list test extended permit tcp object-group SRC-SRV-1155061119 object-group DST-SRV-1155061119 object-group TCP-1155061119

====

Sorting by SCR IP or DST IP is also available.
```
