print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionatio - chaves")
for chave in pessoa.keys():
  print(chave)

print("\nFor utilizando dicionatio - valores")
for valor in pessoa.values():
  print(valor)

print("\nFor utilizando dicionatio - items")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

