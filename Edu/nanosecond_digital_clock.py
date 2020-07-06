f = open("input_ndc.txt", 'r')
data = f.readlines()
f.close()


def get_num_of_leds(num):
    num = str(num)
    res = 0
    for i in num:
        res += num_of_leds[int(i)]
    return res


num_of_leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
diff_num_of_leds = [-4, 3, 0, -1, 1, 1, -3, 4, -1, 0]

min_n = '00000000000'

print(get_num_of_leds(min_n))

n = int(data.pop(0))
leds_on_list = []
for i in range(n):
    leds_on_list.append(int(data.pop(0)))

last_num = diff_num_of_leds.index(leds_on_list[1] - leds_on_list[0])
