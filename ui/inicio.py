from PyQt5 import QtCore, QtGui, QtWidgets
  # Importa la clase MyApp del archivo main.py

class Ui_Inicio(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(396, 457)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 80, 271, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 150, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 230, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "inicio sesion"))
        self.label_2.setText(_translate("Dialog", "nombre de usuario"))
        self.label_3.setText(_translate("Dialog", "contraseña"))
        self.pushButton.setText(_translate("Dialog", "iniciar sesión"))

    def show(self):
        window = QtWidgets.QDialog()
        ui = Ui_Inicio()
        ui.setupUi(window)
        window.show()

if __name__ == "__main__":
    ui = Ui_Inicio()
    ui.show()
