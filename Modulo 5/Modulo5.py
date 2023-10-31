import pandas as pd
import matplotlib.pyplot as plt


def relatorio_vendas(dados_vendas):
  df_vendas = pd.DataFrame(dados_vendas)
  df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])
  df_vendas.set_index('Data', inplace=True)

  df_vendas['Vendas Diárias'].plot(title='Vendas Diárias')
  plt.show()

  df_vendas['Vendas Diárias'].resample('W').sum().plot(title='Vendas Semanais')
  plt.show()

  df_vendas['Vendas Diárias'].resample('M').sum().plot(title='Vendas Mensais')
  plt.show()


def analise_desempenho(dados_desempenho):
  media_tempo_execucao = dados_desempenho['Tempo de Execução'].mean()
  media_satisfacao_cliente = dados_desempenho['Satisfação do Cliente'].mean()

  print(f"Tempo Médio de Execução: {media_tempo_execucao}")
  print(f"Satisfação Média do Cliente: {media_satisfacao_cliente}")


def analise_energetica(dados_energeticos):
  economia_energia_solar = dados_energeticos['Economia Solar'].sum()

  print(
      f"Economia proporcionada pela energia solar: {economia_energetica_solar}"
  )


def mdl5():
  while True:
    print("Menu:")
    print("1. Gerar Relatório de Vendas")
    print("2. Analisar Desempenho de Serviços Automotivos")
    print("3. Analisar Eficiência Energética")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
      dados_vendas = {
          '': [],
          'Vend': [],
        
      }
      relatorio_vendas(dados_vendas)
    elif opcao == '2':
      dados_desempenho = {
          'Serviço': ['Troca de óleo', 'Reparo de motor'],
          'Tempo de Execução': [45, 90],
          'Satisfação do Cliente': [4.5, 4.0]
      }
      analise_desempenho(dados_desempenho)
    elif opcao == '3':
      dados_energeticos = {'Economia Solar': [5000, 6000, 7000]}
      analise_energetica(dados_energeticos)
    elif opcao == '4':
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
  mdl5()
