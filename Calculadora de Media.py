# Inicializa a soma das notas e o contador de notas
soma_notas = 0  # Variável para armazenar a soma total das notas
contador_notas = 0  # Variável para contar quantas notas foram inseridas

# Solicita o nome do usuário
nome = input("Insira seu nome: ")  # Coleta o nome do usuário para personalizar a saída

# Solicita a primeira nota
nota = float(input("Insira a nota: "))  # Solicita uma nota ao usuário e a converte para float
soma_notas += nota  # Adiciona a nota à soma total
contador_notas += 1  # Incrementa o contador de notas

while True:
    # Solicita ao usuário se deseja continuar inserindo notas
    resposta = input("Deseja inserir uma nova nota? (SIM/NÃO): ").strip().upper()  # Coleta a resposta e padroniza para maiúsculas
    if resposta == "SIM":
        nota = float(input("Insira a nota: "))  # Solicita uma nova nota ao usuário
        soma_notas += nota  # Adiciona a nova nota à soma total
        contador_notas += 1  # Incrementa o contador de notas
    elif resposta == "NÃO":
        # Calcula e exibe a média das notas
        if contador_notas > 0:  # Verifica se pelo menos uma nota foi inserida
            media = soma_notas / contador_notas  # Calcula a média das notas
            # Determina o resultado baseado na média
            if media >= 7:
                resultado = "Aprovado"  # Resultado se a média for 7 ou mais
            elif 5 < media < 7:
                resultado = "Recuperação"  # Resultado se a média estiver entre 5 e 7
            else:
                resultado = "Reprovado"  # Resultado se a média for 5 ou menos
            # Exibe o nome do usuário,a quantidade de notas digitadas, a somatória, a média final e o resultado
            print(f"{nome} você digitou ao todo {contador_notas} notas, sendo a somatória {soma_notas},e sua média final: {media:.2f}. O seu resultado é: {resultado}")
        else:
            # Exibe uma mensagem se nenhuma nota foi inserida
            print("Nenhuma nota foi inserida.")
        break  # Encerra o loop
    else:
        # Exibe uma mensagem de erro se a resposta não for válida
        print("Resposta inválida. Por favor, responda com 'SIM' ou 'NÃO'.")
