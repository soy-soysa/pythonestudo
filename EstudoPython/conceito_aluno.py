# Este programa recebe 4 notas, calcula a média e retorna o conceito aprovado, provado ou em recuperação, seguindo os seguintes parâmetros:
# Se a média for >=7 aprovado!
# Se a média for <=4 Reprovado!
# Se a média estiver entre >4 e <7 Recuperação!

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Criando as variáveis
portugues = input("Digite a nota do aluno de português: ")
matematica = input("Digite a nota do aluno nessa matemática: ")
historia = input("Digite a nota do aluno nessa história: ")
ingles = input("Digite a nota do aluno nessa inglês: ")

# Transformando as variáveis de STR para FLT
portugues = float(portugues)
matematica = float(matematica)
historia = float(historia)
ingles = float(ingles)

# Fazer os cálculos das variáveis
somar = portugues + matematica + historia + ingles
media = somar / 4

# Mostrar resultado para o usuário com base no que foi pedido
# Aqui pode se usar >: elif OU >: if
if media >=7:
    print(f"({media}) O aluno está aprovado!")
elif media <=4:
    print(f"({media}) O aluno está reprovado!")
else:
    print(f"({media}) O aluno está de recuperação!")

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Fim do Código