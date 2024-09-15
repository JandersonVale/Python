# Exibe uma mensagem para o usuário indicando que o programa vai identificar o tipo de triângulo
print("Qual é o tipo do triângulo? Vamos descobrir!")
# Solicita ao usuário a medida do primeiro lado do triângulo e converte a entrada para um número de ponto flutuante (float)
l1 = float(input("Insira a medida do lado 1: "))
# Solicita ao usuário a medida do segundo lado do triângulo e converte a entrada para um número de ponto flutuante (float)
l2 = float(input("Insira a medida do lado 2: "))
# Solicita ao usuário a medida do terceiro lado do triângulo e converte a entrada para um número de ponto flutuante (float)
l3 = float(input("Insira a medida do lado 3: "))
# Verifica se todos os lados são iguais
if l1 == l2 == l3:
    # Se todos os lados são iguais, imprime que o triângulo é equilátero
    print("O triângulo é equilátero.")
# Verifica se todos os lados são diferentes
elif l1 != l2 and l2 != l3 and l1 != l3:
    # Se todos os lados são diferentes, imprime que o triângulo é escaleno
    print("O triângulo é escaleno.")
# Se não for equilátero nem escaleno, então é isósceles
else:
    # Imprime que o triângulo é isósceles
    print("O triângulo é isósceles.")
