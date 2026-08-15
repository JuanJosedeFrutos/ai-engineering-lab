with open ("datos_python.txt") as file:
    count = 0
    
    for line in file:
        line = line.lower().strip()
        if "python" in line:
            count += 1

print (count)