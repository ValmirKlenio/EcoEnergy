import csv

class Mercaria:
    def __init__(self):
        self.produtos = {}
        self.carregar_csv()

    def adicionar_produto(self, nome, quantidade, detalhes):
        if nome in self.produtos:
            self.produtos[nome]['quantidade'] += quantidade
        else:
            self.produtos[nome] = {'quantidade': quantidade, 'detalhes': detalhes}
        self.salvar_csv()

    def vender_produto(self, nome, quantidade):
        if nome in self.produtos and self.produtos[nome]['quantidade'] >= quantidade:
            self.produtos[nome]['quantidade'] -= quantidade
            self.salvar_csv()
        else:
            print(f"Produto {nome} não disponível em quantidade suficiente!")

    def reestocar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome]['quantidade'] += quantidade
            self.salvar_csv()
        else:
            print(f"Produto {nome} não encontrado!")

    def listar_produtos(self):
        for produto, detalhes in self.produtos.items():
            print(f"Produto: {produto}, Quantidade: {detalhes['quantidade']}, Detalhes: {detalhes['detalhes']}")

    def analisar_produto(self, nome):
        if nome in self.produtos:
            print(self.produtos[nome])
        else:
            print(f"Produto {nome} não encontrado!")

    def salvar_csv(self, filename="produtos.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Quantidade', 'Detalhes'])
            for produto, info in self.produtos.items():
                writer.writerow([produto, info['quantidade'], info['detalhes']])
                
    def carregar_csv(self, filename="produtos.csv"):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Ignora a linha de cabeçalho
                for row in reader:
                    nome, quantidade, detalhes = row
                    self.produtos[nome] = {'quantidade': int(quantidade), 'detalhes': detalhes}
        except FileNotFoundError:
            pass  # Arquivo não existe ainda, ignorar

if __name__ == "__main__":
    mercaria = Mercaria()

    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Vender produto")
        print("3. Reestocar produto")
        print("4. Listar produtos")
        print("5. Analisar produto")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            detalhes = input("Detalhes: ")
            mercaria.adicionar_produto(nome, quantidade, detalhes)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            mercaria.vender_produto(nome, quantidade)

        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            mercaria.reestocar_produto(nome, quantidade)

        elif opcao == "4":
            mercaria.listar_produtos()

        elif opcao == "5":
            nome = input("Nome do produto para análise: ")
            mercaria.analisar_produto(nome)

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")
