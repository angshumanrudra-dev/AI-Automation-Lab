## This is used when repetition depends on condition, not fixed count.
##
# How while loop works

#Step 1 → check condition
#Step 2 → run code
#Step 3 → update variable
#Step 4 → repeat

#If you forget update → infinite loop

# Use while loop when:

# • You don’t know number of repetitions
# • Loop depends on user input
# • Loop depends on system state

# i = 1   ##Starting point.

# while i <= 5:  ## Loop continues while condition is True.
#     print(i)
#     i = i + 1  ##Moves loop toward termination.Without this → infinite loop.



# password = ""
# while password != "admin":
#     password = input("Enter Password:  ")
# print("password matched")

#print even numbers from 2 to 10 using while loop

i=1
while i <= 10:
    if i %2 == 0:
        print(i)
    i= i+1