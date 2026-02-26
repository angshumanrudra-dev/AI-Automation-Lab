# Sum of First N Numbers (Accumulator Pattern)

# number = int(input("Enter upto the number you want accumulation: "))
# i=0
# total = 0
# while i<=number :
#     total = total +i
#     i=i+1
# print(total)


number = int(input("Enter upto the number you want accumulation: "))
total = 0

for i in range (1,number+1):
    total = total + i

print (total)