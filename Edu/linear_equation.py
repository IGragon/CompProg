f = open("input_le.txt", 'r')
data = f.readlines()
f.close()

a, b, c = map(lambda x: x.strip(), data.pop(0).split())

max_len = max([len(a), len(b), len(c)])
a, b, c = a.rjust(max_len, '0'), b.rjust(max_len, '0'), c.rjust(max_len, '0')

a, b, c = map(list, [a, b, c])
a.reverse()
b.reverse()
c.reverse()

while '?' in a or '?' in b or '?' in c:
    shift = 0
    for i in range(max_len):
        if a[i] == '?' and b[i] != '?' and c[i] != '?':
            d = int(c[i]) - int(b[i]) - shift
            if d < 0:
                d = 10 + d
                shift = 1
            a[i] = str(d)
        elif a[i] != '?' and b[i] == '?' and c[i] != '?':
            d = int(c[i]) - int(a[i]) - shift
            if d < 0:
                d = 10 + d
                shift = 1
            b[i] = str(d)
        elif a[i] != '?' and b[i] != '?' and c[i] == '?':
            d = int(a[i]) + int(b[i]) + shift
            shift = d // 10
            d = d % 10
            c[i] = str(d)
        elif a[i] != '?' and b[i] != '?' and c[i] != '?':
            d = int(a[i]) + int(b[i])
            shift = d // 10

    shift = 0
    for i in range(max_len):
        if a[i] == '?' and b[i] == '?' and c[i] != '?':
            if i != max_len - 1:
                if a[i + 1] != '?' and b[i + 1] != '?' and c[i + 1] != '?':
                    if int(c[i + 1]) - (int(a[i + 1]) + int(b[i + 1])) == 1 or int(c[i + 1]) + 10 - (int(a[i + 1]) + int(b[i + 1])) == 1:
                        a[i] = '9'
                    else:
                        a[i] = '0'
                else:
                    a[i] = '0'
            else:
                a[i] = '1'
        elif a[i] == '?' and b[i] != '?' and c[i] == '?':
            if i != max_len - 1:
                if a[i + 1] != '?' and b[i + 1] != '?' and c[i + 1] != '?':
                    if int(c[i + 1]) - (int(a[i + 1]) + int(b[i + 1])) == 1 or int(c[i + 1]) + 10 - (int(a[i + 1]) + int(b[i + 1])) == 1:
                        a[i] = '9'
                    else:
                        a[i] = '0'
                else:
                    a[i] = '0'
            else:
                a[i] = '1'
        elif a[i] != '?' and b[i] == '?' and c[i] == '?':
            if i != max_len - 1:
                if a[i + 1] != '?' and b[i + 1] != '?' and c[i + 1] != '?':
                    if int(c[i + 1]) - (int(a[i + 1]) + int(b[i + 1])) == 1 or int(c[i + 1]) + 10 - (int(a[i + 1]) + int(b[i + 1])) == 1:
                        b[i] = '9'
                    else:
                        b[i] = '0'
                else:
                    b[i] = '0'
            else:
                b[i] = '1'
        elif a[i] == '?' and b[i] == '?' and c[i] == '?':
            if i != max_len - 1:
                if a[i + 1] != '?' and b[i + 1] != '?' and c[i + 1] != '?':
                    if int(c[i + 1]) - (int(a[i + 1]) + int(b[i + 1])) == 1 or int(c[i + 1]) + 10 - (int(a[i + 1]) + int(b[i + 1])) == 1:
                        a[i] = '9'
                    else:
                        a[i] = '0'
                else:
                    a[i] = '0'
            else:
                c[i] = str(shift + 2)
                a[i] = '1'
                b[i] = str(int(c[i]) - int(a[i]))
        else:
            shift = (int(a[i]) + int(b[i])) // 10

a.reverse()
b.reverse()
c.reverse()
a, b, c = map(lambda x: ''.join(x), (a, b, c))
a, b, c = map(int, (a, b, c))
if a + b == c:
    print(a, b, c)
else:
    print("NO")

# HOMEWORK!!!
