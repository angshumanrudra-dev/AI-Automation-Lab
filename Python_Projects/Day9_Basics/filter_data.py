with open("test.txt", "r") as file:
    for line in file:
        name = line.strip()
        if name.startswith("a"):
          print(name)