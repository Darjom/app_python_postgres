from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        
        # Agregar un layout a la ventana principal (QDialog)
        layout = QtWidgets.QVBoxLayout(Dialog)
  

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(600, 0, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.label2.setFont(font)
        self.label2.setObjectName("label")

        altura=70 #definimos la altura de los botones
        alturaPerfil=200
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20,altura, 150, 41))
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setVisible(False)
        #self.pushButton.clicked.connect(self.home_button_clicked)
        
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(170, altura, 150, 41))
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setVisible(False)
        #self.pushButton2.clicked.connect(self.estudiante_button_clicked)


        self.pushButton3 = QtWidgets.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(320, altura, 150, 41))
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setVisible(False)
        #self.pushButton3.clicked.connect(self.docente_button_clicked)


        self.pushButton4 = QtWidgets.QPushButton(Dialog)
        self.pushButton4.setGeometry(QtCore.QRect(470, altura, 150, 41))
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setVisible(False)
        #self.pushButton4.clicked.connect(self.rol_button_clicked)


        for numUi in self.ui_list:
            numUi=numUi[0]
            if numUi == 1:
                
                self.pushButton.setVisible(True)

            if numUi == 2:
                
                self.pushButton2.setVisible(True)

            if numUi == 3:
                self.pushButton3.setVisible(True)

            if numUi == 4:
                self.pushButton4.setVisible(True)


        self.lineEditNombre = QtWidgets.QLineEdit(Dialog)
        self.lineEditNombre.setGeometry(QtCore.QRect(20, alturaPerfil, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEditNombre.setFont(font)
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.lineEditNombre.setVisible(True)
        
        self.lineEditApellido = QtWidgets.QLineEdit(Dialog)
        self.lineEditApellido.setGeometry(QtCore.QRect(170, alturaPerfil, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEditApellido.setFont(font)
        self.lineEditApellido.setObjectName("lineEditApellido")
        self.lineEditApellido.setVisible(True)

        self.lineEditUsername = QtWidgets.QLineEdit(Dialog)
        self.lineEditUsername.setGeometry(QtCore.QRect(320, alturaPerfil, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditUsername.setVisible(True)

        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(470, alturaPerfil, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)  # Para ocultar la contraseña
        self.lineEditPassword.setVisible(True)

        self.labelNombre = QtWidgets.QLabel(Dialog)
        self.labelNombre.setGeometry(QtCore.QRect(20, alturaPerfil-40, 150, 20))  # Ajusta la posición y el tamaño según tus necesidades
        self.labelNombre.setFont(font)
        self.labelNombre.setObjectName("labelNombre")
        self.labelNombre.setText("Nombre")
        self.labelNombre.setVisible(True)

        self.labelApellido = QtWidgets.QLabel(Dialog)
        self.labelApellido.setGeometry(QtCore.QRect(170, alturaPerfil-40, 150, 20))
        self.labelApellido.setFont(font)
        self.labelApellido.setObjectName("labelApellido")
        self.labelApellido.setText("Apellido")
        self.labelApellido.setVisible(True)

        self.labelUsername = QtWidgets.QLabel(Dialog)
        self.labelUsername.setGeometry(QtCore.QRect(320, alturaPerfil-40, 150, 20))
        self.labelUsername.setFont(font)
        self.labelUsername.setObjectName("labelUsername")
        self.labelUsername.setText("Username")
        self.labelUsername.setVisible(True)

        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setGeometry(QtCore.QRect(470, alturaPerfil-40, 150, 20))
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.labelPassword.setText("Password")
        self.labelPassword.setVisible(True)
        
        self.pushButton5 = QtWidgets.QPushButton(Dialog)
        self.pushButton5.setGeometry(QtCore.QRect(320,alturaPerfil+100, 150, 41))
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setVisible(True)

        self.labelClases = QtWidgets.QLabel(Dialog)
        self.labelClases.setGeometry(QtCore.QRect(200, alturaPerfil-40, 400, 400))
        self.labelClases.setFont(font)
        self.labelClases.setObjectName("labelClases")
        self.labelClases.setVisible(False)

        self.labelGrupos = QtWidgets.QLabel(Dialog)
        self.labelGrupos.setGeometry(QtCore.QRect(200, alturaPerfil-40, 400, 400))
        self.labelGrupos.setFont(font)
        self.labelGrupos.setObjectName("labelGrupos")
        self.labelGrupos.setVisible(False)

        self.lineEditInscribir = QtWidgets.QLineEdit(Dialog)
        self.lineEditInscribir.setGeometry(QtCore.QRect(320, alturaPerfil, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEditInscribir.setFont(font)
        self.lineEditInscribir.setObjectName("lineEditUsername")
        self.lineEditInscribir.setVisible(False)

        self.pushButton6 = QtWidgets.QPushButton(Dialog)
        self.pushButton6.setGeometry(QtCore.QRect(470, alturaPerfil, 150, 41))
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton4")
        self.pushButton6.setVisible(False)

        self.lineEditCrear = QtWidgets.QLineEdit(Dialog)
        self.lineEditCrear.setGeometry(QtCore.QRect(320, alturaPerfil, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEditCrear.setFont(font)
        self.lineEditCrear.setObjectName("lineEditUsername")
        self.lineEditCrear.setVisible(False)

        self.pushButton7 = QtWidgets.QPushButton(Dialog)
        self.pushButton7.setGeometry(QtCore.QRect(470, alturaPerfil, 150, 41))
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName("pushButton4")
        self.pushButton7.setVisible(False)

        self.labelMaterias = QtWidgets.QLabel(Dialog)
        self.labelMaterias.setGeometry(QtCore.QRect(200, alturaPerfil-40, 400, 400))
        self.labelMaterias.setFont(font)
        self.labelMaterias.setObjectName("labelClases")
        self.labelMaterias.setVisible(False)

        Dialog.setLayout(layout)  # Establecer el layout en el QDialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sesión Iniciada"))
        self.label.setText(_translate("Dialog", f"Sesión Iniciada {self.username}"))
        self.label2.setText(_translate("Dialog", f"PID {self.pid}"))
        self.pushButton.setText(_translate("Dialog", "Home"))
        self.pushButton2.setText(_translate("Dialog", "Estudiante"))
        self.pushButton3.setText(_translate("Dialog", "Docente"))
        self.pushButton4.setText(_translate("Dialog", "Materias"))
        self.pushButton5.setText(_translate("Dialog", "Guardar"))
        self.pushButton6.setText(_translate("Dialog", "Inscribir"))
        self.pushButton7.setText(_translate("Dialog", "Crear Materia"))
        self.lineEditNombre.setText(_translate("Dialog", f"{self.nombre}"))
        self.lineEditApellido.setText(_translate("Dialog", f"{self.apellido}"))
        self.lineEditUsername.setText(_translate("Dialog", f"{self.username}"))
        self.lineEditPassword.setText(_translate("Dialog", f"{self.password}"))
        self.labelClases.setText("Clases Inscritas:\n")
        for clase in self.clases:
            clase_text = f"{clase[0]}, Materia: {clase[1]}"
            self.labelClases.setText(f"{self.labelClases.text()}\n{clase_text}")
        
        self.labelGrupos.setText("Perteneces a los siguientes Grupos:\n")
        for grupo in self.grupos:
            clase_text = f"{grupo[0]}, Materia: {grupo[1]}"
            self.labelGrupos.setText(f"{self.labelGrupos.text()}\n{clase_text}")
        self.labelMaterias.setText("Existen las siguientes materias")
        for materia in self.materias:
            clase_text = f"Materia: {materia[1]}"
            self.labelMaterias.setText(f"{self.labelMaterias.text()}\n{clase_text}")
        

    def off_home(self):
        self.lineEditNombre.setVisible(False)
        self.labelNombre.setVisible(False)
        self.lineEditApellido.setVisible(False)
        self.labelApellido.setVisible(False)
        self.lineEditUsername.setVisible(False)
        self.labelUsername.setVisible(False)
        self.lineEditPassword.setVisible(False)
        self.labelPassword.setVisible(False)
        self.pushButton5.setVisible(False)

    def on_home(self):
        self.lineEditNombre.setVisible(True)
        self.labelNombre.setVisible(True)
        self.lineEditApellido.setVisible(True)
        self.labelApellido.setVisible(True)
        self.lineEditUsername.setVisible(True)
        self.labelUsername.setVisible(True)
        self.lineEditPassword.setVisible(True)
        self.labelPassword.setVisible(True)
        self.pushButton5.setVisible(True)

    def off_estudiante(self):
        self.labelClases.setVisible(False)
        self.lineEditInscribir.setVisible(False)
        self.pushButton6.setVisible(False)

    def on_estudiante(self):
        self.labelClases.setVisible(True)
        self.lineEditInscribir.setVisible(True)
        self.pushButton6.setVisible(True)

    def on_docente(self):
        self.labelGrupos.setVisible(True)
        self.lineEditCrear.setVisible(True)
        self.pushButton7.setVisible(True)
    
    def off_docente(self):
        self.labelGrupos.setVisible(False)
        self.lineEditCrear.setVisible(False)
        self.pushButton7.setVisible(False)
    
    def on_Materia(self):
        self.labelMaterias.setVisible(True)

    def off_Materia(self):
        self.labelMaterias.setVisible(False)

    def set_ui_list(self, ui_list):
        self.ui_list = ui_list

    def set_username(self, username):
        self.username = username

    def set_pid(self, pid):
        self.pid = pid
    
    def set_password(self, password):
        self.password=password
    
    def set_nombre(self, nombre):
        self.nombre=nombre

    def set_apellido(self, apellido):
        self.apellido=apellido

    def clases_inscrito(self,clases):
        self.clases=clases

    def clases_revision(self,grupos):
        self.grupos=grupos

    def set_materia(self,materias):
        self.materias=materias


    def home_button_clicked(self):
        self.on_home()
        self.off_estudiante()
        self.off_docente()
        self.off_Materia()

    def estudiante_button_clicked(self):
        self.off_home()
        self.off_docente()
        self.on_estudiante()
        self.off_Materia()

    def docente_button_clicked(self):
        self.off_home()
        self.off_estudiante()
        self.on_docente()
        self.off_Materia()


    def rol_button_clicked(self):
        self.off_home()
        self.off_docente()
        self.off_estudiante()
        self.on_Materia()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = QtWidgets.QDialog()
    ui = Ui_Home()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())