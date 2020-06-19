from string import ascii_uppercase as abc
f = open("input_cg2.txt", 'r')
data = f.readlines()
f.close()

l, max_mistakes = map(int, data.pop(0).split())

letters = data.pop(0).strip()
letters_counter = [0 for _ in range(26)]
mistakes = 0

for letter in letters:
    index = abc.index(letter)
    if index > 0:
        if letters_counter[index - 1] > 0:
            letters_counter[index] += 1
            letters_counter[index - 1] -= 1
        else:
            letters_counter[index] += 1
            mistakes += 1
    else:
        letters_counter[index] += 1

print(mistakes)
print("TOO MUCH MISTAKES" if mistakes > max_mistakes else "THAT'S ALRIGHT")
