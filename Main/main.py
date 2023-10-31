import csv
import os

estoque = []

# MENU CENTRAL
def menu():
  print('''Escolha uma opção:
  1. Controle de Estoque
  2. Gerenciamento de Serviços Automotivos
  3. Gestão da Mercearia
  4. Monitoramento Estratégico
  5. Relatórios e Análises
  6. Encerrar''')

# CONTROLE DE ESTOQUE

def menu_controle_estoque():
  print('''Escolha uma opção:
  1. Cadastrar Produto
  2. Atualizar Produto
  3. Excluir Produto
  4. Listar Produtos
  5. ENCERRAR''')

def adicionar():
  print('..:: ADICONANDO PRODUTOS AO ESTOQUE ::..')
  produto = input('Produto: ')
  preco = float(input('Preço: '))
  quantidade = input('Quantidade: ')
  estoque.append({'produto': produto, 'preço': preco, 'quantidade': quantidade})
  print(estoque)
  if produto in estoque:
    produto += quantidade
  with open('produtos.csv', 'w', newline='') as arq_prod:
    escritor_csv = csv.writer(arq_prod)
    escritor_csv.writerows(estoque)
    print(escritor_csv)
  try:
    with open('produtos.csv', 'r') as arq:
      leitor_csv = arq.read()
      print(leitor_csv)
  except FileNotFoundError as erro:
    print(f'Erro: {erro}. O arquivo não foi encontrado.')

def verificar():
  produto = input('Produto que deseja verificar: ')
  for prod in estoque:
      produto, preco, quantidade = prod
      print(prod)

def vender():
  produto = input('Produto: ')
  for produto, preco, quantidade in estoque:
    print(f'Produto: {produto}, Peço: {preco}, Quantidade: {quantidade}')
    opc = input('Deseja vender esse produto? ')
    if opc == 'Ss' or opc == 'Sim' or opc == 'sim' or opc == 'SIM':
        estoque[produto] -= quantidade
    else:
        if estoque[produto] >= 3:
          print("Quantidade insuficiente no estoque.")

def listar_produtos():
  print(" ..:: Produtos no estoque ::..")
  for p in estoque:
    produto, peco, quantidade = p
    print(p)

# CONTROLE DE ESTOQUE

# GERENCIAMENTO DE SERVIÇOS

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

# Funções de Arquivo .csv
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

# GERENCIAMENTO DE SERVIÇOS

# GESTÃO MERCEARIA

class Mercaria:
  def __init__(self):
      self.produtos = {}

  def adicionar_produto(self, nome, quantidade, detalhes):
      if nome in self.produtos:
          self.produtos[nome]['quantidade'] += quantidade
      else:
          self.produtos[nome] = {'quantidade': quantidade, 'detalhes': detalhes}

  def vender_produto(self, nome, quantidade):
      if nome in self.produtos and self.produtos[nome]['quantidade'] >= quantidade:
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
          print(f"Produto: {produto}, Quantidade: {detalhes['quantidade']}, Detalhes: {detalhes['detalhes']}")

  def analisar_produto(self, nome):
      if nome in self.produtos:
          print(self.produtos[nome])
      else:
          print(f"Produto {nome} não encontrado!")

if __name__ == "__main__":
  mercaria = Mercaria()

# GESTÃO MERCEARIA

# Função de Menu
def exibir_menu():
    print("\nMENU:")
    print("1. Agendar Serviço")
    print("2. Listar Serviços Disponíveis")
    print("3. Sair")

arquivo_servicos = "servicos.csv"
servicos = carregar_csv(arquivo_servicos)
mecanico = Mecanico("José")

while True:
  menu()
  opcao = int(input('Opção: '))
  if opcao == 1: # CONTROLE DE ESTOQUE
    menu_controle_estoque()
    opc = int(input('Opção: '))
    # validação
    while opc < 1 and opc > 5:
        opc = int(input('ERRO! Digite um número entre 1 e 7: '))
    # cadastro de produtos
    if opc == 1:
        print('...::: Cadastro Produtos :::...')
        print()
        adicionar()
        print('-*' * 20)
    # verificação do estoque
    elif opc == 2:
        print('-*' * 20)
        print('...::: Atualização Estoque :::...')
        print()
        verificar()
        print('-*' * 20)
    # vendas e remoção de produto
    elif opc == 3:
        print('-*' * 20)
        print('...::: Venda e Excusão de Produtos :::...')
        print()
        vender()
        print('-*' * 20)
    # listar produtos do estoque
    elif opc == 4:
      print('-*' * 20)
      print('...::: Listagem Produtos :::...')
      print()
      listar_produtos()
      print('-*' * 20)
    # encerrar
    elif opc == 5:
        print('-*' * 20)
        print('...::: ENCERRANDO :::...')
        print('-*' * 20)
        break
  elif opcao == 2: # GERENCIAMENTO DE SERVIÇOS
      exibir_menu()
      opcao_g = input("Escolha uma opção: ")
      if opcao_g == 1:
          print("Serviços disponíveis:")
          for i, servico in enumerate(servicos, 1):
              print(f"{i}. {servico}")

          escolha = int(input("Escolha o número do serviço: ")) - 1

          if 0 <= escolha < len(servicos):
              data_hora = input("Data e Hora do Serviço (exemplo: 2023-10-31 14:00): ")
              veiculo = Veiculo(input("Placa do Veículo: "), input("Modelo do Veículo: "))
              servico_escolhido = servicos[escolha]

              # Agendamento do serviço
              with open("agenda.txt", "a") as file:
                  file.write(f"{mecanico}, {servico_escolhido}, {veiculo}, {data_hora}\n")
              print("Serviço agendado com sucesso!")

          else:
              print("Escolha inválida.")

      elif opcao_g == 2:
          print("Serviços disponíveis:")
          for i, servico in enumerate(servicos, 1):
              print(f"{i}. {servico}")

      elif opcao_g == 3:
          print("Saindo do programa.")
          break

      else:
          print("Opção inválida. Escolha novamente.")
  elif opcao == 3: # GERENCIAMENTO DA MERCEARIA
      menu_mercearia()
      opcao_mg = int(input('Opção:'))
      if opcao_mg == "1":
          nome = input("Nome do produto: ")
          quantidade = int(input("Quantidade: "))
          detalhes = input("Detalhes: ")
          mercaria.adicionar_produto(nome, quantidade, detalhes)

      elif opcao_mg == 2:
          nome = input("Nome do produto: ")
          quantidade = int(input("Quantidade: "))
          mercaria.vender_produto(nome, quantidade)

      elif opcao_mg == 3:
          nome = input("Nome do produto: ")
          quantidade = int(input("Quantidade: "))
          mercaria.reestocar_produto(nome, quantidade)

      elif opcao_mg == 4:
          mercaria.listar_produtos()

      elif opcao_mg == 5:
          nome = input("Nome do produto para análise: ")
          mercaria.analisar_produto(nome)

      elif opcao_mg == 6:
          break

      else:
          print("Opção inválida!")
