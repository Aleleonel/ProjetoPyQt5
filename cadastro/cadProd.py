from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="03120808",
    database="cadastro_produtos"
)


def edit_dados():
    linha = formulario_listprod.tableWidget.currentRow()

    cursor = banco.cursor()
    comando_SQL = "SELECT id FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]

    cursor.execute("SELECT * FROM produtos WHERE id =" + str(valor_id))
    produto = cursor.fetchall()
    formulario_editprod.show()

    formulario_editprod.ld_id.setText(str(produto[0][0]))
    formulario_editprod.ld_codigo.setText(str(produto[0][1]))
    formulario_editprod.ld_produto.setText(str(produto[0][2]))
    formulario_editprod.ld_preco.setText(str(produto[0][3]))
    formulario_editprod.ld_categoria.setText(str(produto[0][4]))


def salvar():
    linha = formulario_listprod.tableWidget.currentRow()

    cursor = banco.cursor()
    comando_SQL = "SELECT id FROM produtos"
    cursor.execute(comando_SQL)

    dados_lidos = cursor.fetchall()

    valor_id = dados_lidos[linha][0]

    cursor.execute("SELECT * FROM produtos WHERE id =" + str(valor_id))
    produto = cursor.fetchall()
    prod = formulario_editprod.ld_produto.text()
    prec = formulario_editprod.ld_preco.text()
    cat = formulario_editprod.ld_categoria.text()

    comando_SQL = "UPDATE produtos SET descricao = '" + prod + "', preco = '" \
                  + prec + "', categoria = '" + cat + "' WHERE id =" + str(valor_id)
    cursor.execute(comando_SQL)
    #
    banco.commit()
    formulario_editprod.close()


def excluir_dados():
    linha = formulario_listprod.tableWidget.currentRow()
    formulario_listprod.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    comando_SQL = "SELECT id FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id =" + str(valor_id))
    banco.commit()


def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Lista de Produtos.pdf")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(200, 800, "Produtos: ")
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(10, 750, "ID")
    pdf.drawString(50, 750, "CODIGO")
    pdf.drawString(110, 750, "PRODUTO")
    pdf.drawString(310, 750, "PREÇO")
    pdf.drawString(410, 750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y += 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(50, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410, 750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("pdf foi salvo com sucesso!")


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
    # limpando todos os campos
    formulario.ldCod.setText("")
    formulario.ldDesc.setText("")
    formulario.ldPrec.setText("")


def listaProd():
    formulario_listprod.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    formulario_listprod.tableWidget.setRowCount(len(dados_lidos))
    formulario_listprod.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            formulario_listprod.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app = QtWidgets.QApplication([])
formulario = uic.loadUi("cadProd.ui")
formulario_listprod = uic.loadUi("listprod.ui")
formulario_editprod = uic.loadUi("editprod.ui")

formulario.btnCadastrar.clicked.connect(principal)
formulario.btnListar.clicked.connect(listaProd)
formulario_listprod.btn_pdf.clicked.connect(gerar_pdf)
formulario_listprod.btnDel.clicked.connect(excluir_dados)
formulario_listprod.btnEditar.clicked.connect(edit_dados)
formulario_editprod.btnSalvarEdit.clicked.connect(salvar)

formulario.show()
app.exec()
