from string import ascii_lowercase as abc
from random import shuffle

f = open("original_text.txt", 'r')
origin_list = f.readlines()
f.close()

key = list(abc)
shuffle(key)
key = ''.join(key)

origin = ""
for i in origin_list:
    origin += i.lower()

encrypted = ""
for i in origin:
    if i in abc:
        encrypted += key[abc.index(i)]
    else:
        encrypted += i

f = open("encrypted_text.txt", 'w')
f.write(encrypted)
f.close()

print(key)
