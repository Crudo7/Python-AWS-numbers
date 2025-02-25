def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Guardar los números primos entre 1 y 250 en una lista
primos = []
for i in range(1, 251):
    if es_primo(i):
        primos.append(i)

# Escribir los resultados en el archivo results.txt
with open('results.txt', 'w') as archivo:
    for primo in primos:
        archivo.write(f"{primo}\n")

# Imprimir los números primos por consola para verificar
print("Números primos entre 1 y 250:")
for primo in primos:
    print(primo)

print("Los números primos han sido guardados en 'results.txt'.")