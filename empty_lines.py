with open ("datos.txt") as archivo:
    count = 0
    for linea in archivo:
        if linea.strip():
            count += 1

print (count)