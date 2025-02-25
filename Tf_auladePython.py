# Dicionário para armazenar os produtos
inventario = {}

# Função para adicionar um produto
def adicionar_produto(nome, preco, quantidade):
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}
    print(f"Produto {nome} adicionado com sucesso!")

# Função para remover um produto
def remover_produto(nome):
    if nome in inventario:
        del inventario[nome]
        print(f"Produto {nome} removido com sucesso!")
    else:
        print(f"Produto {nome} não encontrado no inventário.")

# Função para listar todos os produtos
def listar_produtos():
    if inventario:
        for nome, info in inventario.items():
            print(f"Nome: {nome}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")
    else:
        print("O inventário está vazio.")

# Menu para interagir com o usuário
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            adicionar_produto(nome, preco, quantidade)
        elif opcao == '2':
            nome = input("Nome do produto a ser removido: ")
            remover_produto(nome)
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()