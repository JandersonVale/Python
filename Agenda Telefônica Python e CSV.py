import csv  # Importa o módulo 'csv' para ler e escrever arquivos CSV
import os, sys  # Importa os módulos 'os' e 'sys' para manipulação de sistema e encerramento do programa

# Nome do arquivo CSV que será utilizado
arquivo = "agenda_telefonica.csv"
# Limpa a tela do terminal (cmd ou console) para um ambiente limpo
os.system('cls')# Verifica se o arquivo CSV já existe
if os.path.exists(arquivo):# Se o arquivo já existe, não faz nada
    pass
else:# Se o arquivo não existe, cria o arquivo e escreve o cabeçalho
    with open(arquivo, "a", newline='') as arquivo_csv:
        leitor = csv.writer(arquivo_csv)  # Cria um objeto writer para escrever no arquivo CSV
        leitor.writerow(["Nome", "Telefone", "Endereço"])  # Escreve o cabeçalho no arquivo CSV
    print(f"Arquivo CSV {arquivo} criado.")  # Informa que o arquivo foi criado


while True:# Loop principal do programa
    os.system('cls') # Limpa a tela do terminal
    print("##### MENU #####\n[1] Cadastrar contato\n[2] Consultar contato\n[3] Sair do programa")# Exibe o menu para o usuário
    opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção

    if opcao == "1":  # Se o usuário escolher a opção 1 (Cadastrar contato)
        os.system('cls')  # Limpa a tela do terminal
        # Solicita informações do novo contato
        nome = input("Insira o nome do contato: ")
        telefone = input("Insira o telefone do contato: ")
        endereco = input("Insira o endereço do contato: ")  # Corrigido o nome da variável 'endereço' para 'endereco' (sem acento)
       
        with open(arquivo, "a", newline='') as arquivo_csv: # Abre o arquivo CSV para adicionar o novo contato
            escritor = csv.writer(arquivo_csv)  # Cria um objeto writer para adicionar ao arquivo CSV
            escritor.writerow([nome, telefone, endereco])  # Adiciona a nova linha de contato ao arquivo
            print("Contato gravado com sucesso!\n")  # Informa que os dados foram gravados

        input("Pressione Enter para retornar ao menu principal...")  # Aguarda o usuário pressionar Enter

    elif opcao == "2":  # Se o usuário escolher a opção 2 (Consultar contato)
        os.system('cls')  # Limpa a tela do terminal

        # Abre o arquivo CSV para leitura
        with open(arquivo, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)  # Cria um objeto reader para ler o arquivo CSV
            for linha in leitor:  # Itera sobre cada linha no arquivo CSV
                print(linha)  # Exibe a linha do arquivo CSV
        print("Estes são todos os contatos armazenados.\n")
        input("Pressione Enter para retornar ao menu principal...")  # Aguarda o usuário pressionar Enter

    elif opcao == "3":  # Se o usuário escolher a opção 3 (Sair do programa)
        os.system('cls')  # Limpa a tela do terminal
        print("Programa encerrado.")  # Informa que o programa está sendo encerrado
        sys.exit()  # Encerra o programa

    else:  # Se o usuário escolher uma opção inválida
        os.system('cls')  # Limpa a tela do terminal
        print("Opção inválida. Tente novamente.\n")  # Informa que a opção escolhida é inválida
        input("Pressione Enter para retornar ao menu principal...")  # Aguarda o usuário pressionar Enter
