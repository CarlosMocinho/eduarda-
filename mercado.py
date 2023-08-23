def main():
    lista = []

    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar Item")
        print("2. Editar Item")
        print("3. Apagar Item")
        print("4. Listar Itens")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Digite o nome do item a ser adicionado: ")
            lista.append(item)
            print(f"{item} foi adicionado à lista.")

        elif escolha == "2":
            print("\n--- Itens na Lista ---")
            for index, item in enumerate(lista):
                print(f"{index + 1}. {item}")
            numero_item = int(input("Digite o número do item que deseja editar: ")) - 1
            if 0 <= numero_item < len(lista):
                novo_iten = input("Digite o novo nome do item: ")
                lista[numero_item] = novo_iten
                print("Item editado com sucesso.")
            else:
                print("Número de item inválido.")

        elif escolha == "3":
            print("\n--- Itens na Lista ---")
            for index, item in enumerate(lista):
                print(f"{index + 1}. {item}")
            numero_item = int(input("Digite o número do item que deseja apagar: ")) - 1
            if 0 <= numero_item < len(lista):
                remover_item = lista.pop(numero_item)
                print(f"{remover_item} foi removido da lista.")
            else:
                print("Número de item inválido.")

        elif escolha == "4":
            print("\n--- Itens na Lista ---")
            for index, item in enumerate(lista):
                print(f"{index + 1}. {item}")

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
