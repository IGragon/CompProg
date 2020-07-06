print("Enter values in order <starting sum>, <annual addition>, <annual percent>, <duration in years>")
start_sum, annual_addition, percent, duration = map(int, input().split())

percent = percent / 100
total_sum = start_sum

print("Starting sum:", start_sum)

for i in range(duration):
    start_sum += annual_addition
    total_sum += annual_addition + percent * total_sum + 0.13 * annual_addition
    print("After", i + 1, 'year(s):', total_sum)

print()
print("Total sum after", duration, "years:", total_sum)
print("Spent", start_sum)
print("Clear earnings", total_sum - start_sum)
