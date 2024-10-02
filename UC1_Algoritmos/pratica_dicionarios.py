# IMPORTANDO OS

import os
os.system("cls")

# ATIVIDADE 1 - TESTANDO DICIONÁRIOS

contatos_lista = [('Gustavo', '1234 5678'), ('Pedro', '9999 9999'), ('Ana', '8765 4321'), ('Marina', '7788 8877')]

contatos = dict(contatos_lista)

print(contatos)

print(contatos["Marina"])

# Em caso de contrato não encontrado

print(contatos.get("Chuck","Não encontrado"))

atores_lista = [("Chris Evans", "Capitão América"), ("Mark Ruffalo", "Hulk"), ("Tom Hiddleston", "Loki"), ("Chris Hemworth", "Thor"), ("Robert Downey Jr", "Homem de Ferro"), ("Scarlett Johansson", "Viúva Negra")]

atores = dict(atores_lista)

print(atores)

print("Hulk" in atores.values()) # Retorna false ou true

# Adicionando e excluindo valores

atores["Robert Pattinson"] = "Batman"

print(atores)

del atores["Robert Pattinson"]

print(atores.pop("Sonny Jim", "Contato não encontrado"))

print(atores)

# Unindo listas

contatos_yan_lista = [('Samir', '1234 5678'), ('Ladir', '9999 9999'), ('Bandir', '8765 4321'), ('Tambir', '7788 8877')]

contatos_yan = dict(contatos_yan_lista)

contatos.update(contatos_yan)

print(contatos)

