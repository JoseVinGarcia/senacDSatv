# ATIVIDADE 2 - Loja de Roupas
import pandas as pd

# Criando lista com Valores
produtos = ["Camiseta", "Calça", "Jaqueta", "Vestido", "Boné"]
quantidade = [50,30,15,10,25]

# Transformando em série
sestoque = pd.Series(quantidade, index = produtos)

# Adicionando valor nulo
sestoque.loc["Saia"] = None

# Mostrando estoque inteiro
print("="*30)
print("ESTOQUE TOTAL:")
print(sestoque)

# Mostrando produtos com mais de 20 unidades
print("\nPRODUTOS COM MAIS DE UNIDADE:")
print(sestoque[sestoque>20])

# Adicionando valores
svalores=pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

# Mostrando o estoque agora com valores
print("\nPRODUTOS COM PREÇO:")
print(svalores)

# Exibindo o valor total
print("\nVALOR TOTAL DO ESTOQUE:")
print(sestoque * svalores)
