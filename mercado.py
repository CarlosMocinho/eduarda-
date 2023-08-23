def main():
    shopping_list = []

    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar Item")
        print("2. Editar Item")
        print("3. Apagar Item")
        print("4. Listar Itens")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == "1":
            item = input("Digite o nome do item a ser adicionado: ")
            shopping_list.append(item)
            print(f"{item} foi adicionado à lista.")

        elif choice == "2":
            print("\n--- Itens na Lista ---")
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
            item_number = int(input("Digite o número do item que deseja editar: ")) - 1
            if 0 <= item_number < len(shopping_list):
                new_item = input("Digite o novo nome do item: ")
                shopping_list[item_number] = new_item
                print("Item editado com sucesso.")
            else:
                print("Número de item inválido.")

        elif choice == "3":
            print("\n--- Itens na Lista ---")
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
            item_number = int(input("Digite o número do item que deseja apagar: ")) - 1
            if 0 <= item_number < len(shopping_list):
                removed_item = shopping_list.pop(item_number)
                print(f"{removed_item} foi removido da lista.")
            else:
                print("Número de item inválido.")

        elif choice == "4":
            print("\n--- Itens na Lista ---")
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")

        elif choice == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
