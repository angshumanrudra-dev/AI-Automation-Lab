#number list analyzer. write program that shows sum , max, min, average
#take numbers as input for the list
numbers= []
n= int(input("How many numbers you want in the list? "))
for i in range(1,n+1):
    num1= int(input("Tell me a number: "))
    numbers.append(num1)
print(numbers)
#sum of the number
total = 0
for num in numbers:
    total = total + num 
print (f"SUM : {total}")
#Max num in the list
max_value= numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

print (f"Max Value: {max_value}")

#Min num in the list
min_value= numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print (f"Min Value: {min_value}")

#Average of the list.
length = len(numbers)
print (f"Average: {total/length}")