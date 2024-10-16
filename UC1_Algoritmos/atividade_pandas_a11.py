import pandas as pd

# ATIVIDADE AULA 11 - DATASET

# Lendo e imprimindo
df = pd.read_csv("imdb.csv", sep=",", encoding="utf-8")
print(df)

# Filtrando
dfe=df[df["averageRating"] > 8.0]
print(dfe)

# Exportando
dfe.to_excel("imdb_editado.xls", index=False, engine="openpyxl")
