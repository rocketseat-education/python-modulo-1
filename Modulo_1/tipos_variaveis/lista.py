# Declaracao

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista
minha_lista[0] = "python"
print("minha_lista[0]:", minha_lista)

print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7]) # minha_lista[1], minha_lista[2], ...minha_lista[6]
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6)", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert: Insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort
# minha_lista = [1, 10, 3, 3, 5, 6, 7, 8, 112]
minha_lista.sort()
print("Após sort()", minha_lista)