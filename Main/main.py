import csv
import os

estoque = []


class Mecanico:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (R${self.preco:.2f})"


class Veiculo:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

    def __str__(self):
        return f"{self.modelo} ({self.placa})"


def salvar_csv(servicos, arquivo):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Preço"])
        for servico in servicos:
            writer.writerow([servico.nome, servico.preco])


def carregar_csv(arquivo):
    servicos = []
    if os.path.exists(arquivo):
        with open(arquivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                servicos.append(Servico(row["Nome"], float(row["Preço"])))
    return servicos


def menu():
    while True:
        print('''Escolha uma opção:
        1. Controle de Estoque
        2. Gerenciamento de Serviços Automotivos
        3. Sair''')

        opcao = input('Opção? ')

        if opcao == '1':
            menu_controle_estoque()

        elif opcao == '2':
            menu_gerenciamento_servicos()

        elif opcao == '3':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Escolha novamente.")


def menu_controle_estoque():
    while True:
        print('''Escolha uma opção:
        1. Cadastrar Produto
        2. Listar Produtos
        3. Sair''')

        opcao = input('Opção? ')

        if opcao == '1':
            adicionar_produto()

        elif opcao == '2':
            listar_produtos()

        elif opcao == '3':
            break


def adicionar_produto():
    produto = input('Produto: ')
    preco = float(input('Preço: R$'))
    quantidade = int(input('Quantidade: '))
    estoque.append({'produto': produto, 'preço': preco, 'quantidade': quantidade})


def listar_produtos():
    print("Produtos no estoque:")
    for produto in estoque:
        print(f"Produto: {produto['produto']}, Preço: R${produto['preço']}, Quantidade: {produto['quantidade']}")


def menu_gerenciamento_servicos():
    arquivo_servicos = "servicos.csv"
    servicos = carregar_csv(arquivo_servicos)

    while True:
        print('''\nMENU Gerenciamento de Serviços Automotivos:
        1. Agendar Serviço
        2. Listar Serviços Disponíveis
        3. Sair''')

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            agendar_servico(servicos)

        elif opcao == '2':
            listar_servicos(servicos)

        elif opcao == '3':
            break


def agendar_servico(servicos):
    for i, servico in enumerate(servicos, 1):
        print(f"{i}. {servico}")

    escolha = int(input("Escolha o número do serviço: ")) - 1

    if 0 <= escolha < len(servicos):
        data_hora = input("Data e Hora do Serviço (exemplo: 2023-10-31 14:00): ")
        placa_veiculo = input("Placa do Veículo: ")
        modelo_veiculo = input("Modelo do Veículo: ")

        with open("agenda.txt", "a") as file:
            file.write(f"{data_hora}, {placa_veiculo}, {modelo_veiculo}, {servicos[escolha]}\n")

        print("Serviço agendado com sucesso!")


def listar_servicos(servicos):
    print("Serviços disponíveis:")
    for i, servico in enumerate(servicos, 1):
        print(f"{i}. {servico}")


if __name__ == "__main__":
    menu()
