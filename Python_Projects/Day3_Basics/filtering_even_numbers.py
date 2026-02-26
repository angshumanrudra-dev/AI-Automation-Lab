## print only even numbers from 1 to 10

total = 0

for i in range (2,22,2):
    print(i)
    total = total + i

print(total)

for i in range (1,21):
    if i % 2 == 0:
        print(i)