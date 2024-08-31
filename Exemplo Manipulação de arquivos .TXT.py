import sys  # Importa o módulo sys para usar funções relacionadas ao sistema, como sys.exit() para encerrar o script.
import os   # Importa o módulo os para usar funções relacionadas ao sistema operacional, como os.path.exists() para verificar a existência de arquivos e os.system() para executar comandos do sistema.

base = 'dados.txt'  # Define o nome do arquivo onde os dados serão armazenados.

# Verifica se o arquivo já existe no diretório atual
if not os.path.exists(base):
    # Se o arquivo não existir, cria um novo arquivo com o nome definido em 'base'
    with open(base, 'a', encoding='utf-8') as arquivo:
        pass  # 'pass' é um espaço reservado que indica que nada mais será feito aqui. O arquivo é criado e fica pronto para uso.

# Loop While para a criação do menu
while True:
    os.system('cls')  # Limpa a tela do console antes de exibir o menu. 'cls' é o comando para limpar a tela no Windows. No Linux/Mac, o comando seria 'clear'.
    print("#####MENU#####\n[1] Cadastrar\n[2] Consultar\n[3] Sair")  # Exibe as opções do menu para o usuário.
    opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu.

    if opcao == "1":  # Se o usuário escolher a opção 1 (Cadastrar)
        os.system('cls')  # Limpa a tela antes de iniciar a operação de cadastro.
        with open(base, 'a', encoding='utf-8') as arquivo:  # Abre o arquivo em modo de anexação ('a') para adicionar dados ao final.
            dados = input("Insira as informações que deseja:\n")  # Solicita ao usuário que insira os dados que deseja salvar.
            arquivo.write(f'{dados}\n')  # Escreve os dados inseridos pelo usuário no arquivo, adicionando uma nova linha ao final.
            print("Dados gravados com sucesso!")  # Exibe uma mensagem indicando que os dados foram gravados com sucesso.
        input("Pressione Enter para retornar ao menu principal...")  # Pausa o programa e espera que o usuário pressione Enter antes de retornar ao menu principal.

    elif opcao == "2":  # Se o usuário escolher a opção 2 (Consultar)
        os.system('cls')  # Limpa a tela antes de iniciar a operação de consulta.
        with open(base, 'r', encoding='utf-8') as arquivo:  # Abre o arquivo em modo de leitura ('r') para consultar os dados.
            dados = arquivo.read()  # Lê todo o conteúdo do arquivo e armazena na variável 'dados'.
            print(dados)  # Exibe o conteúdo do arquivo para o usuário.
        input("Pressione Enter para retornar ao menu principal...")  # Pausa o programa e espera que o usuário pressione Enter antes de retornar ao menu principal.

    elif opcao == "3":  # Se o usuário escolher a opção 3 (Sair)
        os.system('cls')  # Limpa a tela antes de encerrar o programa.
        print("Programa encerrado.")  # Exibe uma mensagem indicando que o programa está sendo encerrado.
        sys.exit()  # Encerra a execução do script imediatamente. O programa não continuará após esta linha.

    else:  # Se o usuário escolher uma opção inválida
        os.system('cls')  # Limpa a tela antes de exibir a mensagem de erro.
        print("Opção inválida. Tente novamente.")  # Exibe uma mensagem indicando que a opção escolhida é inválida e que o usuário deve tentar novamente.
        input("Pressione Enter para retornar ao menu principal...")  # Pausa o programa e espera que o usuário pressione Enter antes de retornar ao menu principal.
