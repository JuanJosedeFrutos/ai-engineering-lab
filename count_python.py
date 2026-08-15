with open ("datos_python.txt") as file:
    count = 0
    for line in file:
        
        line = line.lower().strip()
        if line == "python":
            count += 1
print (count)
