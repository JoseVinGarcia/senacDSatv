# ATIVIDADE 3 - Leitura e análise
import pandas as pd

# Vamos ler o arquivo dentro do Try Except para não dar cagada :)
try:
    dados = pd.read_excel("vendas_roupas.xlsx")

    # Mostrando os 10 primeiros elementos
    print("="*90)
    print("DADOS DO DATAFRAME:")
    print(dados.head(10))

    # Calculando e exibindo somatório
    print("\nUNIDADES VENDIDAS NO TOTAL:")
    print(dados["Unidades Vendidas"].sum())

    # Calculando e exibindo o valor médio
    print("\nMÉDIA DE PREÇO POR UNIDADE:")
    print(dados["Preço por Unidade (R$)"].mean())

    # Calculando o maior faturamento total entre os produtos:
    
    # 1. Definindo valor de maior faturamento
    fattotal = dados["Faturamento Total (R$)"].max()
    
    # 2. Criando dataframe filtrando pelo valor criado acima
    dffatt = dados[dados["Faturamento Total (R$)"] == fattotal]

    # 3. Exibindo
    print("\nPRODUTO COM MAIOR FATURAMENTO:")
    print(dffatt[["Produto", "Faturamento Total (R$)"]])

    # Calculando o menor faturamento total entre os produtos:
    # Realizando os mesmos passos que fizemos para exibir o maior faturamento!
    fattmin = dados["Faturamento Total (R$)"].min()
    dffatm = dados[dados["Faturamento Total (R$)"] == fattmin]
    print("\nPRODUTO COM MENOR FATURAMENTO:")
    print(dffatm[["Produto", "Faturamento Total (R$)"]])

    # Filtrando e exibindo apenas valores com baixa satisfação:
    dfsat = dados[dados["Satisfação"] == "Baixo"]
    print("\nPRODUTOS COM BAIXA SATISFAÇÃO:")

    # Printando apenas as colunas específicas (Passando valor como lista)
    print(dfsat[["Produto", "Satisfação"]])

except Exception as e:
    print(f"Erro {e}")
    exit()
