# IMPORTANDO OS

import os
os.system("cls")

# ATIVIDADE 1 - CLASSIFICAÇÃO DE PREVISÃO DO TEMPO

dsemana = ["Segunda","Terça","Quarta","Quinta","Sexta"]
previsoes = ["Nublado", "Chuvoso", "Tempestade", "Ensolarado", "Ensolarado"]

diasol = []
diasemsol = []

for e in range(len(previsoes)):
    if previsoes[e] == "Ensolarado":
        diasol.append(dsemana[e])
    else:
        diasemsol.append(dsemana[e])

print("Dias ensolarados:")
for i in diasol:
    print(i)

print("Dias chuvosos:")
for a in diasemsol:
    print(a)
