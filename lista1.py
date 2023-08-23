nums = []
soma = 0

for i in range(5):
    num = int(input("Ensira o {i+1} número inteiro: "))
    nums.append(num)

for num in nums:
    soma += num

print("lista dos numeros:",nums)
print("Soma da lista:",soma)