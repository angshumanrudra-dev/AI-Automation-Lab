with open("test.txt", "r") as file:
    i=1
    for line in file:
        print(i,".",line.strip())
        i=i+1
    