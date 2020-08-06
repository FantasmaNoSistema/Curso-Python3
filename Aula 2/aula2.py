nome = input("Digite seu nome: ")

print("Seu nome é: " + nome)
print("Seu nome é:",nome)
print("Seu nome é: {}".format(nome))
print(f"Seu nome é: {nome}")

#
#   int() transforma em inteiro
#   float() transforma em float
#   str() transforma em string
#   bool() transforma em boolean   
#   list() transforma em lista
#   dict() transforma em dicionario   
#   tuple() transforma em tupla
#

numero = int(input("Digite um número: "))

print(numero + 5) # Adição
print(numero - 2) # Subtração
print(numero * 2) # Multiplicação
print(numero ** 2) # Exponenciação
print(numero / 2) # Divisao (Retorna float)
print(numero // 2) # Divisao (Retorna inteiro)
print(numero % 2) # Modulo