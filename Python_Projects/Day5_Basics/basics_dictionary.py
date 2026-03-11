# Lists store values by position.
# Dictionaries store values by name (key).
# This is extremely useful in automation, databases, APIs, AI systems.

car = {
"brand" : "Toyota",
"model" : "Fortuner",
"year" : 2022
}

# print (car)
# print(car["brand"])
# print(car["year"])

car["color"]="black"
car["model"] = "Legender"
del car["year"]

print(car)


# | Operation         | Syntax                         |
# | ----------------- | ------------------------------ |
# | Create dictionary | `{}`                           |
# | Access value      | `dict["key"]`                  |
# | Add value         | `dict["new_key"] = value`      |
# | Update value      | `dict["existing_key"] = value` |
# | Remove value      | `del dict["key"]`              |
