# ATIVIDADE PARA CASA - RECUPERACAO DE VEICULOS POR CISP

import pandas as pd
import numpy as np
import os

# OBTENDO DADOS
try:
    os.system("cls")
    print("Obtendo dados...")
    ENDERECO_DADOS="https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=";", encoding="iso-8859-1")

    df_recuperacao_cisp = df_ocorrencias[["cisp","recuperacao_veiculos"]]
    df_recuperacao_cisp = df_recuperacao_cisp.groupby(["cisp"]).sum(["recuperacao_veiculos"]).reset_index()

    print("Dados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")
    exit()

# CALCULANDO DADOS
try:
    print("Calculando informações...")

    # Transformando em Array
    array_recuperacao = np.array(df_recuperacao_cisp["recuperacao_veiculos"])

    # Calculando e printando medidas centrais
    media_recuperacao = np.mean(array_recuperacao)
    mediana_recuperacao = np.median(array_recuperacao)
    dist_recuperacao = abs((media_recuperacao-mediana_recuperacao)/mediana_recuperacao)

    print("\nMEDIDAS DE TENDÊNCIA CENTRAL")
    print(f"Média de recuperação de veículos: {media_recuperacao}")
    print(f"Mediana de recuperação de veículos: {mediana_recuperacao}")
    print(f"Distância entre média e mediana: {dist_recuperacao}%")

    # Calculando e printando medidas dispersao
    maximo = np.max(array_recuperacao)
    minimo = np.min(array_recuperacao)
    amplitude = maximo - minimo

    print("\nMEDIDAS DE DISPERSÃO")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Amplitude total: {amplitude}")

    # Calculando e printando medidas de posição
    q1 = np.quantile(array_recuperacao, 0.25, method="weibull")
    q2 = np.quantile(array_recuperacao, 0.50, method="weibull")
    q3 = np.quantile(array_recuperacao, 0.75, method="weibull")
    iqr = q3 - q1

    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    print("\nMEDIDAS DE POSIÇÃO")
    print(f"Mínimo: {minimo}")
    print(f"Limite inferior: {limite_inferior}")
    print(f"Q1: {q1}")
    print(f"Q2: {q2}")
    print(f"Q3: {q3}")
    print(f"IQR: {iqr}")
    print(f"Limite superior: {limite_superior}")
    print(f"Máximo: {maximo}")

    # Descobrindo outliers
    df_recuperacao_out_inf = df_recuperacao_cisp[df_recuperacao_cisp["recuperacao_veiculos"] < limite_inferior]
    df_recuperacao_out_sup = df_recuperacao_cisp[df_recuperacao_cisp["recuperacao_veiculos"] > limite_superior]

    if len(df_recuperacao_out_inf) == 0:
        print("\nSEM CISPS COM OUTLIERS INFERIORES!")
    else:
        print("\nCISPS COM OUTLIERS INFERIORES:")
        print(df_recuperacao_out_inf.sort_values(by="recuperacao_veiculos", ascending=True))

    if len(df_recuperacao_out_sup) == 0:
        print("\nSEM CISPS COM OUTLIERS SUPERIORES")
    else:
        print("\nCISPS COM OUTLIERS SUPERIORES:")
        print(df_recuperacao_out_sup.sort_values(by="recuperacao_veiculos", ascending=False).head(3))

    # RESPONDENDO AO ENUNCIADO
    print("="*30, "\nRESPONDENDO AO ENUNCIADO")
    print("\nNão é possível afirmar um padrão para os dados pois os dados são muito dispersos.")
    print("Porém temos algumas delegacias que tem uma taxa de recuperação acima do normal, como as abaixo:")
    print(df_recuperacao_out_sup.sort_values(by="recuperacao_veiculos", ascending=False).head(3))
    print("\n Quando às delegacias com menor taxa de recuperação, temos:")
    print(df_recuperacao_cisp.sort_values(by="recuperacao_veiculos", ascending=False).tail(3))

except Exception as e:
    print(f"Erro ao obter informações: {e}")
    exit()
