# Vamos trabalhar com as 5 operações aritméticas. Vamos pedir ao usuário 2 valores para realizar nossas operações
valor1 = input("Digite um número inteiro: ")
valor2 = input("Digite outro número inteiro: ")

# Converter String (cadeia de texto) em números inteiros
valor1 = int(valor1)
valor2 = int(valor2)

# Colocando as operações
soma = valor1 + valor2
subtrair = valor1 - valor2
multiplicar = valor1 * valor2
dividir = valor1 / valor2
resto = valor1 % valor2

# Vamos apresentar o resultado fazendo uma interpolação entre texto e as variáveis mostrando o texto literalmente e o conteúdo das variáveis. Utilizaremos o comando 'print'
# com o tipo 'f'(format)
print(f"O resultado da soma é {soma}")
print(f"O resultado da subtração é {subtrair}")
print(f"O resultado da multiplicação é {multiplicar}")
print(f"O resultado da divisão é {dividir}")
print(f"O resto é {resto}")
# Pode usar também >: print("O resultado é "+str(variavel)