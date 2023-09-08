def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

fatorial_de_5 = calcular_fatorial(5)

print(f'O fatorial de 5 é: {fatorial_de_5}')