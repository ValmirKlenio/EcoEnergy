import csv

estoque = []

def menu():
  print('''Escolha uma opção:
  1. Controle de Estoque
  2. Gerenciamento de Serviços Automotivos
  3. Gestão da Merceariag
  4. Monitoramento Estratégico
  5. Relatórios e Análises
  6. Encerrar''')

def menu_controle_estoque():
  print('''Escolha uma opção:
  1. Cadastrar Produto
  2. Atualizar Produto
  3. Excluir Produto
  4. Listar Produtos
  5. ENCERRAR''')

'''class Estoque:
    def __init__(self, produto, preco, quantidade):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade'''

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

while True:
  menu()
  opcao = int(input('Opção? '))
  if opcao == 1:
    menu_controle_estoque()
    opc = int(input('Opção: '))
    # validação
    while opc < 1 and opc > 5:
        opc = int(input('ERRO! Digite um número entre 1 e 7: '))
    # cadastro
    if opc == 1:
        print('...::: Cadastro Produtos :::...')
        print()
        adicionar()
        print('-*' * 20)
    # listar as pessoas
    elif opc == 2:
        print('-*' * 20)
        print('...::: Atualização Estoque :::...')
        print()
        verificar()
        print('-*' * 20)
    # buscar cadastro
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
    # encerrar o cadastro de pessoas
    elif opc == 5:
        print('-*' * 20)
        print('...::: ENCERRANDO :::...')
        print('-*' * 20)
        break
