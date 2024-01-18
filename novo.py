# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode # Adição das Bibliotecas 
from time import sleep


class Ui_MainWindow(object):    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 638)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1) 

        ### Inicio da codificação       

        # Definição das Funções
        def gerar_e_exibir_imagem(): 
            content = self.lineEdit.text() 
            imagem_qrcode = qrcode.make(content)
            imagem_qrcode.save("image.png")               
            carregar_imagem()    
            

        def salvar_img():            
            content = self.lineEdit.text()
            imagem_qrcode = qrcode.make(content)
            imagem_qrcode.save("image.png")            
            carregar_imagem() 
            
            self.lineEdit.setText('')  # Limpar campo 
            arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]            
            imagem_qrcode.save(arquivo)    
            
        def carregar_imagem():
            imagem = QtGui.QPixmap('image.png')  # Carregar a imagem
            cena = QtWidgets.QGraphicsScene()  # Criar uma cena
            item = QtWidgets.QGraphicsPixmapItem(imagem)  # Criar um item com a imagem
            cena.addItem(item)  # Adicionar o item à cena
            self.graphicsView.setScene(cena)  # Definir a cena na graphicsView

        # Definição do que cada botão vai fazer
        self.pushButton.clicked.connect(gerar_e_exibir_imagem)
        self.pushButton_2.clicked.connect(salvar_img)
        

        # Fim da codificação

        MainWindow.setCentralWidget(self.centralwidget)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador de QR-Code"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Digite seu texto ou link..."))
        self.pushButton.setText(_translate("MainWindow", "Gerar QR CODE"))
        self.pushButton_2.setText(_translate("MainWindow", "Salvar QR CODE >>")) 
    




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())