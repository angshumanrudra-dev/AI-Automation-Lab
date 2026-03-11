## A list is a container that stores multiple values in one variable.

numbers = [5 , 15 , 25 , 35 , 45]

print(numbers)

for i in range (0,5,2):
    print (numbers[i])

## Two ways to access list
#  Direct Method 
#  numbers = [5 , 15 , 25 , 35 , 45]
# numbers[2]


#Loop access
numbers = [5 , 15 , 25 , 35 , 45]
for i in range(len(numbers)):
    print(numbers[i])