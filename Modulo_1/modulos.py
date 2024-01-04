print("Exemplo de importação de um módulo padrão:")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")
# import meu_modulo
from meu_modulo import saudacao, dobro
# from meu_modulo import dobro

# mensagem = meu_modulo.saudacao("Gabriel")
# resultado_dobro = meu_modulo.dobro(5)
# print(mensagem)
# print(f"O dobro de 5 é {resultado_dobro}")

mensagem = saudacao("Gabriel")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")