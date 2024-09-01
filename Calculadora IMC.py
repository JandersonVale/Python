
nome = input("Insira seu nome: ") # Solicita ao usuário que insira seu nome e armazena a entrada na variável 'nome'.
peso = float(input("Insira seu peso: ")) # Solicita ao usuário que insira seu peso em quilogramas e converte a entrada para um número de ponto flutuante (float).
altura = float(input("Insira sua altura: ")) # Solicita ao usuário que insira sua altura em metros e converte a entrada para um número de ponto flutuante (float).
# Calcula o Índice de Massa Corporal (IMC) utilizando a fórmula: peso / (altura * altura).
imc = peso / (altura * altura)

if imc < 18.5: # Verifica a faixa do IMC e imprime a classificação correspondente com uma mensagem personalizada.  
    print(f'{nome} seu imc é: {imc:.2f}, sendo o grau considerado com Magreza') # Se o IMC é menor que 18.5, imprime que a pessoa está com Magreza.
elif 18.5 <= imc < 24.9: # Se o IMC está entre 18.5 e 24.9, imprime que a pessoa está com peso Normal.
    print(f'{nome} seu imc é: {imc:.2f}, sendo o grau considerado com Normal')
elif 25 <= imc < 29.9:  # Se o IMC está entre 25 e 29.9, imprime que a pessoa está com Sobrepeso.
    print(f'{nome} seu imc é: {imc:.2f}, sendo o grau considerado com Sobrepeso') 
elif 30 <= imc < 39.9:  # Se o IMC está entre 30 e 39.9, imprime que a pessoa está com Obesidade.
    print(f'{nome} seu imc é: {imc:.2f}, sendo o grau considerado com Obesidade')   
else:  # Se o IMC é 40 ou mais, imprime que a pessoa está com Obesidade Grave.
    print(f'{nome} seu imc é: {imc:.2f}, sendo o grau considerado com Obesidade Grave')
