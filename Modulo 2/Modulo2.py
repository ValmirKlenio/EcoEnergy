import os
import csv

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

def exibir_menu():
    print("\nMENU:")
    print("1. Agendar Serviço")
    print("2. Listar Serviços Disponíveis")
    print("3. Sair")

def main():
    arquivo_servicos = "servicos.csv"
    servicos = carregar_csv(arquivo_servicos)
    mecanico = Mecanico("José")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Serviços disponíveis:")
            for i, servico in enumerate(servicos, 1):
                print(f"{i}. {servico}")

            escolha = int(input("Escolha o número do serviço: ")) - 1

            if 0 <= escolha < len(servicos):
                data_hora = input("Data e Hora do Serviço (exemplo: 2023-10-31 14:00): ")
                placa_veiculo = input("Placa do Veículo: ")
                modelo_veiculo = input("Modelo do Veículo: ")
                veiculo = Veiculo(placa_veiculo, modelo_veiculo)
                servico_escolhido = servicos[escolha]

                with open("agenda.txt", "a") as file:
                    file.write(f"{mecanico}, {servico_escolhido}, {veiculo}, {data_hora}\n")
                print("Serviço agendado com sucesso!")

            else:
                print("Escolha inválida.")

        elif opcao == '2':
            print("Serviços disponíveis:")
            for i, servico in enumerate(servicos, 1):
                print(f"{i}. {servico}")

        elif opcao == '3':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
