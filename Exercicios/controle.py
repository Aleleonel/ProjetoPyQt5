from PyQt5 import uic, QtWidgets


def func_principal():

    if formulario.radioButton.isChecked():
        opcao = 'Azul'
    elif formulario.radioButton_2.isChecked():
        opcao = 'Amarelo'
    elif formulario.radioButton_3.isChecked():
        opcao = 'Branco'
    elif formulario.radioButton_4.isChecked():
        opcao = 'Verde'
    else:
        opcao = 'Nenhuma radio button foi selecionado'

    formulario.lblResp.setText(opcao)


app = QtWidgets.QApplication([])
formulario=uic.loadUi("janela01.ui")
formulario.btnEnviar.clicked.connect(func_principal)

formulario.show()
app.exec()
