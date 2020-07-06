f = open("input_elevator.txt", 'r')
data = f.readlines()
f.close()

speed_up, speed_down = map(int, data.pop(0).split())
speed_elevator = int(data.pop(0))
n = int(data.pop(0))

x = (-speed_up * (n * speed_up + n * speed_down + speed_down)) / (speed_elevator * speed_down - speed_up ** 2 - 2 * speed_up * speed_down)
y = (x * (speed_elevator + speed_down) + speed_up) / (speed_up + speed_down)

max_time = []

x_current = int(x)
y_current = int(y)
upper_floor = x_current * speed_elevator + (n - x_current) * speed_up
up = speed_up * (y_current - 1)
down = x_current * speed_elevator + (x_current - y_current) * speed_down
max_time.append(max([upper_floor, up, down]))

x_current = int(x) + 1
y_current = int(y)
upper_floor = x_current * speed_elevator + (n - x_current) * speed_up
up = speed_up * (y_current - 1)
down = x_current * speed_elevator + (x_current - y_current) * speed_down
max_time.append(max([upper_floor, up, down]))

x_current = int(x)
y_current = int(y) + 1
upper_floor = x_current * speed_elevator + (n - x_current) * speed_up 
up = speed_up * (y_current - 1)
down = x_current * speed_elevator + (x_current - y_current) * speed_down
max_time.append(max([upper_floor, up, down]))

x_current = int(x) + 1
y_current = int(y) + 1
upper_floor = x_current * speed_elevator + (n - x_current) * speed_up
up = speed_up * (y_current - 1)
down = x_current * speed_elevator + (x_current - y_current) * speed_down
max_time.append(max([upper_floor, up, down]))

print(min(max_time))
