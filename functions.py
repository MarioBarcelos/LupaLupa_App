# importações
import os
import sys

# importando SQLite
import sqlite3
from sqlite3 import Error

# Importando PYSIDE2 ou PYSIDE6
if 'PySide2' in sys.modules:
    from PySide2.QtWidgets import *
    
elif 'PySide6' in sys.modules:
    from PySide6.QtWidgets import *
    

class AppFuntions():
    """docstring para AppFunctions"""
    def __init__(self, arg):
        super(AppFuntions, self).__init__()
        self.arg = arg

    # Criando coneção com Banco de Dados
    def create_connection(db_file):
        """ criando uma coneção com Banco de Dados utilzando um Banco de Dados 'SQLite' """
        conn = None 
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn 
    
    # Criando tabela
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    # Função Main 
    def main(dbFolder):
        # Criando Tabela caso não exista
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users (
                                            USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            USER_NAME TEXT,
                                            USER_EMAIL TEXT,
                                            USER_PHONE TEXT,
                                        );
                                    """
        # Criando conexão com db
        conn = AppFuntions.create_connection(dbFolder)

        # criando tabelas 
        if conn is not None:
            # criando tabela de usuario
            AppFuntions.create_table(conn, create_user_table)

        else:
            print("Erro! Não é possível criar conexão com o banco de dados.")
    
    # buscando todos os Usuarios do DB
    def getAllUsers(dbFolder):
        # criando conexão com db
        conn = AppFuntions.create_connection(dbFolder)

        get_all_users = """
                            SELECT * FROM Users;
                        """
        try:
            c = conn.cursor()
            c.execute(get_all_users)
            # retornando todas as linhas da tabela
            return c 
        except Error as e:
            print(e)

    # Adicionando usuários ao Banco de Dados
    def addUser(self, dbFolder):
        # Criando conexão com db
        conn = AppFuntions.create_connection(dbFolder)

        # Buscando valores do formulário
        autor = self.ui.autor.text()
        destinatario = self.ui.destinatario.text()
        local = self.ui.local.text()

        # Criando instrução SQL
        insert_person_data_sql = f"""
                                INSERT INTO Users (USER_NAME, USER_EMAIL, USER_PHONE) 
                                VALUES ('{autor}', '{destinatario}', '{local}');
                                """
        
        # Executando instrução SQL
        if not conn.cursor().execute(insert_person_data_sql):
            print("Não foi possível inserir os dados desta pessoa!")
        else:
            conn.commit()
            # Limpando o formulário de entrada
            self.ui.autor.setText("")
            self.ui.destinatario.setText("")
            self.ui.local.setText("")
            
            # Carregando novo usuário do banco de dados para exibir na tabela
            AppFuntions.displayUsers(self, AppFuntions.getAllUsers(dbFolder))
    
    # Exibindo usuarios
    def displayUsers(self, rows):
        # Loop para percorrer todas as linhas
        for row in rows:
            # Buscando número de linhas
            rowPosition = self.ui.tableWidget.rowCount()

            # Ignorando linhas que já foram carregadas na tabela
            if rowPosition+1 > row[0]:
                continue

            itemCount = 0
            # Criando nova linha na tabela
            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # Adicionando itens na linha
            for item in row:
                self.qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.ui.tableWidget.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount = itemCount+1

            rowPosition = rowPosition+1
