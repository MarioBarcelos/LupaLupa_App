import os 
import sys
import json

# Importando o arquivo GUI
from user_interface import *

# Importando os Widgets customizados
from Custom_Widgets.Widgets import *

#Iniciando as configurações do App
settings = QSettings()

from functions import AppFuntions

#  Class da Janela principal 
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_centralWidget()
        self.ui.setupUi(self)

        # Usando JSON
        loadJsonStyle(self, self.ui, jsonFiles = {"style.json"})

        # Exibindo a janela
        self.show()

        # Reaplicando novas Configurações
        QAppSettings.updateAppSettings(self)

        # Pasta e Nome do DB
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/3MSolutions_DB.db'))
        
        # Executando a função principal para criar o banco de dados e a tabela
        AppFuntions.main(dbFolder)
        
        # Exibindo as linhas do db na tabela
        AppFuntions.displayUsers(self, AppFuntions.getAllUsers(dbFolder))
        
        # Adicionando novo Usuario no DB
        self.ui.addUserBtn.clicked.connect(lambda: AppFuntions.addUser(self, dbFolder))




# Executando o APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())