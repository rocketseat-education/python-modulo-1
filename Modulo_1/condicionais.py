# if, elif e else

# Exemplo de "if"
idade = 18
print("Exemplo de comando if")
if idade >= 18:
  print("Você é maior de idade.")
elif idade >= 12:
  print("Você é um adolescente")
else:
  print("Você é menor de idade.")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)

# if idade == 19:
#   print("Você tem 19 anos")

# if idade < 18:
#   print("Você é menor de idade")

# if idade != 10:
#   print("Você não tem 10 anos")