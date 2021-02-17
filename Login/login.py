# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela03.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    #
    # STYLES
    #

    stylelineEditeOk = ("QLineEdit {    \n"
                        "        border: 2px solid rgb(45, 45, 45);\n"
                        "        border-radius: 5px;\n"
                        "        padding: 15px;    \n"
                        "        background-color: rgb(30, 30, 30);\n"
                        "        color: rgb(100, 100, 100);        \n"
                        "}\n"
                        "QLineEdit:hover {    \n"
                        "        border: 2px solid rgb(55, 55, 55);\n"
                        "}\n"
                        "QLineEdit:focus {    \n"
                        "        border: 2px solid rgb(255, 207, 0);        \n"
                        "        color: rgb(243, 243, 243);\n"
                        "}")

    stylelineEditeError = ("QLineEdit {    \n"
                           "        border: 2px solid rgb(233, 185, 110);\n"
                           "        border-radius: 5px;\n"
                           "        padding: 15px;    \n"
                           "        background-color: rgb(30, 30, 30);\n"
                           "        color: rgb(100, 100, 100);        \n"
                           "}\n"
                           "QLineEdit:hover {    \n"
                           "        border: 2px solid rgb(55, 55, 55);\n"
                           "}\n"
                           "QLineEdit:focus {    \n"
                           "        border: 2px solid rgb(255, 207, 0);        \n"
                           "        color: rgb(243, 243, 243);\n"
                           "}")

    stylePopupError = "background-color: rgb(255, 85, 127); border-radius: 5px;"
    stylePopupOk = "background-color: rgb(0, 255, 123); border-radius: 5px;"

    #
    # FUNCTION
    #

    def checkFields(self):
        V_User = ""
        V_Password = ""

        def showMessage(message):
            self.frm_error.show()
            self.lbl_error.setText(message)

        # VERIFICA USUÁRIO
        if not self.txtuser.text():
            V_User = " Usuário em branco. "
            self.txtuser.setStyleSheet(self.stylelineEditeError)
        else:
            V_User = ""
            self.txtuser.setStyleSheet(self.stylelineEditeOk)

        # VERIFICA SENHA
        if not self.txtpassword.text():
            V_Password = " Senha em branco. "
            self.txtpassword.setStyleSheet(self.stylelineEditeError)
        else:
            V_Password = ""
            self.txtpassword.setStyleSheet(self.stylelineEditeOk)

        # VERIFICA CAMPO
        if V_User + V_Password != "":
            texto = V_User + V_Password
            showMessage(texto)
            self.frm_error.setStyleSheet(self.stylePopupError)
        else:
            texto = "Login Ok"
            if self.chksave.isChecked():
                texto += "| Saver user: ok"
            showMessage(texto)
            self.frm_error.setStyleSheet(self.stylePopupOk)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/Icones/icone-login.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(5, 52, 24);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frm_error = QtWidgets.QFrame(self.top_bar)
        self.frm_error.setMaximumSize(QtCore.QSize(450, 16777215))

        # alerado
        self.frm_error.setStyleSheet(self.stylePopupError)

        self.frm_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_error.setObjectName("frm_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frm_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_error = QtWidgets.QLabel(self.frm_error)
        self.lbl_error.setStyleSheet("color: rgb(46, 52, 54);")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.horizontalLayout_3.addWidget(self.lbl_error)
        self.btnfechar = QtWidgets.QPushButton(self.frm_error)
        self.btnfechar.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnfechar.setFont(font)
        self.btnfechar.setStyleSheet("QPushButton {\n"
                                     "        border-radius: 5px;        \n"
                                     "        background-position: center;        \n"
                                     "        background-image: url(:/close_image/sair.svg);\n"
                                     "        background-color: rgb(60, 60, 60);\n"
                                     "        \n"
                                     "}\n"
                                     "QPushButton:hover {    \n"
                                     "        background-color: rgb(60, 60, 60);    \n"
                                     "        color: rgb(200, 200, 200);\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "        background-color: rgb(35, 35, 35);    \n"
                                     "        color: rgb(200, 200, 200);\n"
                                     "}")
        self.btnfechar.setText("")
        self.btnfechar.setObjectName("btnfechar")
        self.horizontalLayout_3.addWidget(self.btnfechar)
        self.horizontalLayout_2.addWidget(self.frm_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("background-color: rgb(58, 58, 58);\n"
                                      "border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.perfil = QtWidgets.QFrame(self.login_area)
        self.perfil.setGeometry(QtCore.QRect(170, 170, 111, 101))
        self.perfil.setStyleSheet("QFrame {\n"
                                  "        background-image: url(:/close_image/Imagens/eu.jpg);\n"
                                  "        border-radius: 50px;\n"
                                  "        border: 2px solid rgb(255, 207, 0);\n"
                                  "        background-repeat: no-repeat;\n"
                                  "        background-position: center;\n"
                                  "}\n"
                                  "QFrame:hover {        \n"
                                  "        border: 2px solid rgb(255, 255, 0);        \n"
                                  "}")
        self.perfil.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.perfil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.perfil.setObjectName("perfil")
        self.frmdolar = QtWidgets.QFrame(self.login_area)
        self.frmdolar.setGeometry(QtCore.QRect(170, 30, 121, 121))
        self.frmdolar.setStyleSheet("QFrame    {        \n"
                                    "        background-image: url(:/logo/icones menu/movimentacoes.bmp);\n"
                                    "        border-radius: 50px;\n"
                                    "        border: 2px solid rgb(255, 207, 0);\n"
                                    "        background-repeat: no-repeat;\n"
                                    "        background-position: center;\n"
                                    "}")
        self.frmdolar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmdolar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmdolar.setObjectName("frmdolar")
        self.txtuser = QtWidgets.QLineEdit(self.login_area)
        self.txtuser.setGeometry(QtCore.QRect(85, 290, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtuser.setFont(font)

        # aleração aqui css
        self.txtuser.setStyleSheet(self.stylelineEditeOk)

        self.txtuser.setMaxLength(32)
        self.txtuser.setObjectName("txtuser")
        self.txtpassword = QtWidgets.QLineEdit(self.login_area)
        self.txtpassword.setGeometry(QtCore.QRect(85, 342, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtpassword.setFont(font)

        # aqui recorte
        self.txtpassword.setStyleSheet(self.stylelineEditeOk)

        self.txtpassword.setMaxLength(16)
        self.txtpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtpassword.setObjectName("txtpassword")
        self.chksave = QtWidgets.QCheckBox(self.login_area)
        self.chksave.setGeometry(QtCore.QRect(85, 395, 281, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chksave.setFont(font)
        self.chksave.setStyleSheet("QCheckBox:: indicator {\n"
                                   "        border: 3px solid rgb(100, 100, 100);\n"
                                   "        width: 15px;\n"
                                   "        height: 15px;\n"
                                   "        border-radius: 15px;    \n"
                                   "        background-color: rgb(135, 135, 135);\n"
                                   "}\n"
                                   "QCheckBox:: indicator:checked {\n"
                                   "        border: 3px solid rgb(255, 205, 0);\n"
                                   "        background-color: rgb(255, 255, 0);\n"
                                   "}")
        self.chksave.setObjectName("chksave")
        self.btnlogin = QtWidgets.QPushButton(self.login_area)
        self.btnlogin.setGeometry(QtCore.QRect(85, 425, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnlogin.setFont(font)
        self.btnlogin.setStyleSheet("QPushButton { \n"
                                    "        background-color: rgb(50, 50, 50);\n"
                                    "        border: 2px solid rgb(60,60,60);\n"
                                    "        border-radius: 5px;\n"
                                    "}\n"
                                    "QPushButton:hover { \n"
                                    "        background-color: rgb(60, 60, 60);\n"
                                    "        border: 2px solid rgb(70, 70, 70);\n"
                                    "}\n"
                                    "QPushButton:pressed { \n"
                                    "        background-color: rgb(250, 230, 0);\n"
                                    "        border: 2px solid rgb(255, 165, 24);\n"
                                    "        color: rgb(35, 35, 35);\n"
                                    "}")
        self.btnlogin.setObjectName("btnlogin")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(6, 75, 5);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblrodape = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblrodape.setFont(font)
        self.lblrodape.setStyleSheet("color: rgb(75, 75, 75);")
        self.lblrodape.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblrodape.setObjectName("lblrodape")
        self.verticalLayout_2.addWidget(self.lblrodape)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        #
        # FUNCTIONS
        #

        # BTN CLOSE POPUP - fecha a mensagem de erro
        self.btnfechar.clicked.connect(lambda: self.frm_error.hide())

        # HIDE ERROR - oculta o frame de mensagem de error
        self.frm_error.hide()

        # BOTÃO DE LOGIN
        self.btnlogin.clicked.connect(self.checkFields)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lbl_error.setText(_translate("MainWindow", "error"))
        self.txtuser.setPlaceholderText(_translate("MainWindow", "USER"))
        self.txtpassword.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.chksave.setText(_translate("MainWindow", "SAVE USER"))
        self.btnlogin.setText(_translate("MainWindow", "LOGIN"))
        self.lblrodape.setText(_translate("MainWindow", "Bionic Black-Info"))


import files_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
