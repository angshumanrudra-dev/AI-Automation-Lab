numbers = [12, 45, 7, 89, 23]
total =0
for num in numbers:
    total=total+num
print(f"Total :{total}")

max_value=numbers[0]

for num in numbers:
    if num> max_value:
        max_value = num
print(f"Max value: {max_value}")


min_value=numbers[0]

for num in numbers:
    if num< min_value:
        min_value = num
print(f"Min value: {min_value}")