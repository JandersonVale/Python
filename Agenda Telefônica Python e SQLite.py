import sqlite3  # Importa o módulo 'csv' para ler e escrever arquivos CSV
import os, sys  # Importa os módulos 'os' e 'sys' para manipulação de sistema e encerramento do programa

# Nome do arquivo CSV que será utilizado
banco = "agenda_telefonica2.db"
# Limpa a tela do terminal (cmd ou console) para um ambiente limpo
os.system('cls')# Verifica se o arquivo CSV já existe
if os.path.exists(banco):# Se o arquivo já existe, não faz nada
    print(f'O banco {banco} já existe.')
else:# Se o banco não existe, cria o o mesmo e a tabela
    connect = sqlite3.connect(banco)
    query = connect.cursor()
    query.execute('''CREATE TABLE Contatos(
	ID INTEGER NOT NULL UNIQUE,
	NOME TEXT(50) NOT NULL,
	TELEFONE TEXT(11) NOT NULL,
	ENDERECO TEXT(50),
	PRIMARY KEY(ID AUTOINCREMENT))''')
    connect.commit()
    print(f"Arquivo CSV {banco} criado.")  # Informa que o banco foi criado

while True:# Loop principal do programa
    os.system('cls') # Limpa a tela do terminal
    print("##### MENU #####\n[1] Cadastrar contato\n[2] Consultar contato\n[3] Sair do programa")# Exibe o menu para o usuário
    opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção

    if opcao == "1":  # Se o usuário escolher a opção 1 (Cadastrar contato)
        os.system('cls')  # Limpa a tela do terminal
        # Solicita informações do novo contato
        nome = input("Insira o nome do contato: ")
        telefone = input("Insira o telefone do contato: ")
        if len(telefone) > 11:
            print("O Telefone precisa ter 11 digitos apenas.")
            return  
        endereco = input("Insira o endereço do contato: ")  # Corrigido o nome da variável 'endereço' para 'endereco' (sem acento)

        connect = sqlite3.connect(banco)
        query = connect.cursor()
        query.execute(f"INSERT INTO Contatos (NOME,TELEFONE,ENDERECO) VALUES ('{nome}','{telefone}','{endereco}')")
        connect.commit()

        input("Pressione Enter para retornar ao menu principal...")  # Aguarda o usuário pressionar Enter

    elif opcao == "2":  # Se o usuário escolher a opção 2 (Consultar contato)
        os.system('cls')  # Limpa a tela do terminal

        connect = sqlite3.connect(banco)
        query = connect.cursor()
        query.execute('SELECT * FROM Contatos')
        dados = query.fetchall()
        for data in dados:
            print(data)



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