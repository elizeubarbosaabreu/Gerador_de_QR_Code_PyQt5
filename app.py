from PyQt5 import uic, QtWidgets, QtGui
import qrcode
from time import sleep


def gerar_e_exibir_imagem(): 
    content = janela.lineEdit.text() 
    imagem_qrcode = qrcode.make(content)
    imagem_qrcode.save("image.png")   
    
    carregar_imagem()    
    

def salvar_img():
    
    content = janela.lineEdit.text()
    imagem_qrcode = qrcode.make(content)
    imagem_qrcode.save("image.png")
    
    carregar_imagem() 
    
    janela.lineEdit.setText('')  # Limpar campo  

    arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]
    
    imagem_qrcode.save(arquivo)    
    
def carregar_imagem():
    imagem = QtGui.QPixmap('image.png')  # Carregar a imagem
    cena = QtWidgets.QGraphicsScene()  # Criar uma cena
    item = QtWidgets.QGraphicsPixmapItem(imagem)  # Criar um item com a imagem
    cena.addItem(item)  # Adicionar o item à cena
    janela.graphicsView.setScene(cena)  # Definir a cena na graphicsView




app = QtWidgets.QApplication([])
janela = uic.loadUi("/home/elizeu/Workspace/Gerador_de_QR_Code_PyQt5/template.ui")


janela.pushButton.clicked.connect(gerar_e_exibir_imagem)
janela.pushButton_2.clicked.connect(salvar_img)


janela.show()
app.exec()
