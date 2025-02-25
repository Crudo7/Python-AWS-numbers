def es_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):  # Solo comprobar impares
        if num % i == 0:
            return False
    return True

# Obtener números primos entre 1 y 250 con list comprehension
primos = [i for i in range(1, 251) if es_primo(i)]

# Escribir los resultados en 'results.txt' de manera eficiente
with open('results.txt', 'w') as archivo:
    archivo.writelines(f"{primo}\n" for primo in primos)

# Imprimir los números primos en consola
print("Números primos entre 1 y 250:")
print(", ".join(map(str, primos)))

print("Los números primos han sido guardados en 'results.txt'.")