import csv

class Mercaria:

  def __init__(self):
    self.produtos = {}

  def adicionar_produto(self, nome, quantidade, detalhes):
    if nome in self.produtos:
      self.produtos[nome]['quantidade'] += quantidade
    else:
      self.produtos[nome] = {'quantidade': quantidade, 'detalhes': detalhes}

  def vender_produto(self, nome, quantidade):
    if nome in self.produtos and self.produtos[nome][
        'quantidade'] >= quantidade:
      self.produtos[nome]['quantidade'] -= quantidade
    else:
      print(f"Produto {nome} não disponível em quantidade suficiente!")

  def reestocar_produto(self, nome, quantidade):
    if nome in self.produtos:
      self.produtos[nome]['quantidade'] += quantidade
    else:
      print(f"Produto {nome} não encontrado!")

  def listar_produtos(self):
    for produto, detalhes in self.produtos.items():
      print(
          f"Produto: {produto}, Quantidade: {detalhes['quantidade']}, Detalhes: {detalhes['detalhes']}"
      )

  def importar_csv(self, arquivo):
    try:
      with open(arquivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Ignora a linha do cabeçalho
        for row in reader:
          nome, quantidade, detalhes = row
          self.adicionar_produto(nome, int(quantidade), detalhes)
    except FileNotFoundError:
      print(f"Arquivo {arquivo} não encontrado!")

  def exportar_csv(self, arquivo):
    with open(arquivo, mode='w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(["Nome", "Quantidade", "Detalhes"])  # Cabeçalho
      for nome, info in self.produtos.items():
        writer.writerow([nome, info['quantidade'], info['detalhes']])


if __name__ == "__main__":
  mercaria = Mercaria()

  while True:
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Vender produto")
    print("3. Reestocar produto")
    print("4. Listar produtos")
    print("5. Importar produtos de CSV")
    print("6. Exportar produtos para CSV")
    print("7. Sair")

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
      arquivo = input("Nome do arquivo CSV para importar: ")
      mercaria.importar_csv(arquivo)

    elif opcao == "6":
      arquivo = input("Nome do arquivo CSV para exportar: ")
      mercaria.exportar_csv(arquivo)

    elif opcao == "7":
      break

    else:
      print("Opção inválida!")
