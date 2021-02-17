from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="03120808",
    database="cadastro_produtos"
)


def principal():
    codigo = formulario.ldCod.text()
    descricao = formulario.ldDesc.text()
    preco = formulario.ldPrec.text()
    Categoria = ""

    if formulario.rb01.isChecked():
        print("Categoria Unhas foi Selecionada")
        Categoria = "Unhas"

    elif formulario.rb02.isChecked():
        print("Categoria Maquiagens foi Selecionada")
        Categoria = "Maquiagens"

    elif formulario.rb03.isChecked():
        print("Categoria Pele foi Selecionada")
        Categoria = "Pele"

    elif formulario.rb04.isChecked():
        print("Categoria Cabelo foi Selecionada")
        Categoria = "Cabelo"

    print('Cod: ', codigo)
    print('Descrição: ', descricao)
    print('Preço: ', preco)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao,preco,categoria) values (%s, %s, %s, %s)"
    dados = (str(codigo), str(descricao), str(preco), Categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("cadProd.ui")
formulario.btnCadastrar.clicked.connect(principal)

formulario.show()
app.exec()

