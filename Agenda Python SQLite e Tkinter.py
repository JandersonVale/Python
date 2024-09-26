import tkinter as tkr
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# Classe principal da aplicação, herda de tkr.Tk
class FormPrincipal(tkr.Tk):
    def __init__(self):
        super().__init__()  # Inicializa a classe pai
        self.title('Agenda PY')  # Título da janela
        self.geometry('800x600+300+50')  # Tamanho e posição da janela
        self.resizable(False, False)  # Não permite redimensionar a janela

        # Conexão com o banco de dados SQLite
        self.conn = sqlite3.connect('agenda.db')  # Cria ou abre o banco de dados
        self.cursor = self.conn.cursor()  # Cria um cursor para executar comandos SQL
        # Cria a tabela 'contatos' se não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contatos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                endereco TEXT NOT NULL,
                                telefone TEXT NOT NULL)''')
        self.conn.commit()  # Confirma as alterações no banco de dados

        # Configuração da interface gráfica
        frame_topo = tkr.Frame(self, width=200, height=40, bg='red')  # Frame superior
        frame_topo.place(relwidth=1)  # Ocupar toda a largura
        label_topo = tkr.Label(frame_topo, text='Agenda Python', font=('Arial', '15', 'bold'), fg='white', bg='red')  # Label do título
        label_topo.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o texto

        # Frame para dados do contato
        self.label_frame_cont = LabelFrame(self, text='Dados do Contato', font=('Arial', '10', 'bold'), borderwidth=1, relief='solid', height=300)
        self.label_frame_cont.place(relx=0.025, rely=0.090, relwidth=0.75)

        # Frame para ações
        self.label_frame_ac = LabelFrame(self, text='Ações', font=('Arial', '10', 'bold'), borderwidth=1, relief='solid', height=300)
        self.label_frame_ac.place(relx=0.80, rely=0.090, relwidth=0.175)

        # Botões para as ações
        botao_cad = Button(self, text='Cadastrar', width=15, height=2, relief='solid', bd=1, command=self.cadastrar)
        botao_cad.place(relx=0.818, rely=0.16)

        self.is_editing = False  # Atributo para controle do estado de edição
        self.botao_edit = Button(self, text='Editar', width=15, height=2, relief='solid', bd=1, command=self.editar)
        self.botao_edit.place(relx=0.818, rely=0.26)

        botao_del = Button(self, text='Deletar', width=15, height=2, relief='solid', bd=1, command=self.deletar)
        botao_del.place(relx=0.818, rely=0.36)

        botao_sair = Button(self, text='Sair', width=15, height=2, relief='solid', bd=1, command=self.sair)
        botao_sair.place(relx=0.818, rely=0.46)

        # Labels e campos de entrada para o contato
        label_nome = Label(self, text='Nome:')
        label_nome.place(relx=0.047, rely=0.16)

        self.txt_nome = tkr.Entry(self, width=80, relief='solid', bd=1, font=('Arial', '10', 'bold'))
        self.txt_nome.place(relx=0.047, rely=0.20)

        label_endereco = Label(self, text='Endereço:')
        label_endereco.place(relx=0.047, rely=0.26)

        self.txt_endereco = tkr.Entry(self, width=80, relief='solid', bd=1, font=('Arial', '10', 'bold'))
        self.txt_endereco.place(relx=0.047, rely=0.30)

        label_telefone = Label(self, text='Telefone:')
        label_telefone.place(relx=0.047, rely=0.36)

        self.txt_telefone = tkr.Entry(self, width=80, relief='solid', bd=1, font=('Arial', '10', 'bold'))
        self.txt_telefone.place(relx=0.047, rely=0.40)

        # Criação da tabela de contatos
        self.table_con = ttk.Treeview(self, columns=('nome', 'endereco', 'telefone'), show='headings')
        self.table_con.heading('nome', text='Nome', anchor='w')  # Cabeçalho da coluna Nome
        self.table_con.column('nome', width=100, anchor='w')
        self.table_con.heading('endereco', text='Endereço', anchor='w')  # Cabeçalho da coluna Endereço
        self.table_con.column('endereco', width=100, anchor='w')
        self.table_con.heading('telefone', text='Telefone', anchor='w')  # Cabeçalho da coluna Telefone
        self.table_con.column('telefone', width=100, anchor='w')
        self.table_con.place(relx=0.024, rely=0.625, relwidth=0.95, relheight=0.335)

        self.carregar_dados()  # Carrega os dados existentes no banco de dados

    # Método para carregar dados do banco de dados na tabela
    def carregar_dados(self):
        for row in self.table_con.get_children():  # Remove todos os itens da tabela
            self.table_con.delete(row)
        self.cursor.execute("SELECT nome, endereco, telefone FROM contatos")  # Busca os dados
        for row in self.cursor.fetchall():  # Insere os dados na tabela
            self.table_con.insert("", tkr.END, values=row)

    # Método para cadastrar um novo contato
    def cadastrar(self):
        nome = self.txt_nome.get()  # Obtém o nome
        endereco = self.txt_endereco.get()  # Obtém o endereço
        telefone = self.txt_telefone.get()  # Obtém o telefone
        if nome and endereco and telefone:  # Verifica se todos os campos estão preenchidos
            # Insere os dados no banco de dados
            self.cursor.execute("INSERT INTO contatos (nome, endereco, telefone) VALUES (?, ?, ?)", (nome, endereco, telefone))
            self.conn.commit()  # Confirma a operação
            self.carregar_dados()  # Atualiza a tabela
            self.limpar_campos()  # Limpa os campos de entrada
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")  # Aviso se algum campo estiver vazio

    # Método para editar um contato
    def editar(self):
        selected_item = self.table_con.selection()  # Obtém o item selecionado na tabela
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um item para editar.")  # Aviso se nenhum item estiver selecionado
            return

        if not self.is_editing:  # Se não está editando, inicia a edição
            item_values = self.table_con.item(selected_item)['values']  # Obtém os valores do item selecionado
            self.txt_nome.delete(0, tkr.END)  # Limpa o campo de nome
            self.txt_nome.insert(0, item_values[0])  # Preenche o campo de nome
            self.txt_endereco.delete(0, tkr.END)  # Limpa o campo de endereço
            self.txt_endereco.insert(0, item_values[1])  # Preenche o campo de endereço
            self.txt_telefone.delete(0, tkr.END)  # Limpa o campo de telefone
            self.txt_telefone.insert(0, item_values[2])  # Preenche o campo de telefone
            self.botao_edit.config(text='Salvar')  # Muda o texto do botão para 'Salvar'
            self.is_editing = True  # Marca que está em modo de edição
        else:  # Se está editando, confirma a edição
            self.confirmar_edicao(selected_item)

    # Método para confirmar a edição do contato
    def confirmar_edicao(self, selected_item):
        item_values = self.table_con.item(selected_item)['values']  # Obtém os valores do item selecionado
        # Atualiza os dados no banco de dados
        self.cursor.execute("UPDATE contatos SET nome=?, endereco=?, telefone=? WHERE nome=?", 
                            (self.txt_nome.get(), self.txt_endereco.get(), self.txt_telefone.get(), item_values[0]))
        self.conn.commit()  # Confirma a operação
        self.carregar_dados()  # Atualiza a tabela
        self.limpar_campos()  # Limpa os campos de entrada
        self.botao_edit.config(text='Editar')  # Muda o texto do botão de volta para 'Editar'
        self.is_editing = False  # Reseta o estado de edição

    # Método para deletar um contato
    def deletar(self):
        selected_item = self.table_con.selection()  # Obtém o item selecionado
        if selected_item:
            item_values = self.table_con.item(selected_item)['values']  # Obtém os valores do item selecionado
            self.cursor.execute("DELETE FROM contatos WHERE nome=?", (item_values[0],))  # Deleta o contato do banco de dados
            self.conn.commit()  # Confirma a operação
            self.carregar_dados()  # Atualiza a tabela
        else:
            messagebox.showwarning("Aviso", "Selecione um item para deletar.")  # Aviso se nenhum item estiver selecionado

    # Método para limpar os campos de entrada
    def limpar_campos(self):
        self.txt_nome.delete(0, tkr.END)  # Limpa o campo de nome
        self.txt_endereco.delete(0, tkr.END)  # Limpa o campo de endereço
        self.txt_telefone.delete(0, tkr.END)  # Limpa o campo de telefone

    # Método para sair da aplicação
    def sair(self):
        self.conn.close()  # Fecha a conexão com o banco de dados
        self.destroy()  # Encerra a aplicação

# Execução do programa
if __name__ == "__main__":
    app = FormPrincipal()  # Cria uma instância da classe
    app.mainloop()  # Inicia o loop da interface gráfica
