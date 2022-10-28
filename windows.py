gateway = "192.168.1.1"

from os import system
for line in open("list.txt"):
    line = line.replace('\n', '').replace('\r', '')
    system(f"route add {line} {gateway}")
