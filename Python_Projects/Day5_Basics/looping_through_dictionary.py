# Looping through a dictionary

# student = {
#     "name": "Rahul",
#     "age": 21,
#     "marks": 85
# }

# for key in student:
#     print(key, student[key])

fruit_prices = {
    "apple": 120,
    "banana": 40,
    "mango": 100
}

for key in fruit_prices:
    print(key,fruit_prices[key])

# Alternate Method

for key, value in fruit_prices.items():
    print(key, value)