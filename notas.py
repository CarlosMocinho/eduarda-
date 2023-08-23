alu = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota do aluno {nome}: "))
    alu[nome] = nota


somnot = sum(alu.values())
media = somnot / len(alu)

print(f"A média das notas é: {media}")