from string import ascii_lowercase as abc

f = open("data_text.txt", 'r')
data_list = f.readlines()
f.close()

f = open("encrypted_text.txt", 'r')
encrypted_list = f.readlines()
f.close()

probabilities = [0] * 26
key = [0] * 26

data = ""
for i in data_list:
    data += i.lower()

encrypted = ""
for i in encrypted_list:
    encrypted += i.lower()

for i in data:
    if i in abc:
        probabilities[abc.index(i)] += 1
data_sum = sum(probabilities)
probabilities = [probabilities[i] / data_sum for i in range(26)]
probabilities = sorted(list(zip(probabilities, abc)), key=lambda x: x[0])
probabilities = ''.join([probabilities[i][1] for i in range(26)])

for i in encrypted:
    if i in abc:
        key[abc.index(i)] += 1
enc_sum = sum(key)
key = [key[i] / enc_sum for i in range(26)]
key = sorted(list(zip(key, abc)), key=lambda x: x[0])
key = ''.join([key[i][1] for i in range(26)])

decrypted = ""
for i in encrypted:
    if i in abc:
        decrypted += probabilities[key.index(i)]
    else:
        decrypted += i

f = open("decrypted_text.txt", 'w')
f.write(decrypted)
f.close()

print()
print(probabilities)
print(key)

real_key = ''.join(map(lambda x: x[1], sorted(list(zip(probabilities, key)))))
print(real_key)
