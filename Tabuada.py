
numero = int(input("Insira o número que você deseja saber a tabuada: \n")) #Solicita o número do da tabuada desejado pelo usuário, convertendo o input em inteiro
print(f'Segue a tabuada do número {numero}: \n') #imprime mensagem com o número digitado usando f-string e quebra de linha \n
for i in range(1,11): #percorre o loop de 1 a 10
    print(f'{numero} X {i} = {numero*i}') # imprime tabuada percorrendo o loop exibindo o numero x o contador e o resultado da multiplicação
  
