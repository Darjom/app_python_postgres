import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.mainwindow import Ui_Dialog
from database.db import DatabaseManager
from ui.inicio import Ui_Inicio
from ui.home import Ui_Home
from algoritmos import generar_codigo
#pg backend pid
#pyuic5 ui/mainwindow.ui -o ui/mainwindow.py
 
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.db = DatabaseManager(host="localhost", database="tall", user="postgres", password="1234", port="5433")
        self.idUser = None
        self.username=None
        self.password=None

        self.ui.pushButton.clicked.connect(self.insert_user)
        self.ui.pushButton_2.clicked.connect(self.open_inicio_window)

    def insert_user(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        tipo_usuario = self.ui.comboBox.currentText()
        codigo_usuario=generar_codigo()

        self.db.insert_user(username, password)

        id_user=self.db.get_user_id(username)

        if tipo_usuario=="Estudiante":
            self.db.register_user_as_student(id_user,codigo_usuario)    
        if tipo_usuario=="Educador":
            self.db.register_user_as_teacher(id_user)

        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    def open_inicio_window(self):
        self.inicio_window = QtWidgets.QDialog()  # Crea una instancia de QDialog
        ui_inicio = Ui_Inicio()
        ui_inicio.setupUi(self.inicio_window)

        # Conecta el botón "Iniciar Sesión" a la función login
        ui_inicio.pushButton.clicked.connect(self.login)

        self.inicio_window.rejected.connect(self.inicio_window.hide)
        self.inicio_window.rejected.connect(self.open_home)
        
        self.hide()  # Oculta la ventana principal
        self.inicio_window.show()


    def login(self):
        self.username = self.inicio_window.findChild(QtWidgets.QLineEdit, "lineEdit").text()
        self.password = self.inicio_window.findChild(QtWidgets.QLineEdit, "lineEdit_2").text()
        self.idUser = self.db.get_user_id(self.username)
        if self.db.verify_credentials(self.username, self.password):
            self.open_home()
            self.inicio_window.accept()  # Cierra la ventana de inicio
        else:
            QtWidgets.QMessageBox.warning(self, "Inicio de Sesión", "Inicio de sesión no exitoso. Verifica tus credenciales")


    def open_home(self):
        # Realizo la apertura de la siguiente ventana
        self.home_window = QtWidgets.QDialog()
        self.ui_home = Ui_Home()

        if self.username is not None:
            self.ui_home.username=self.username
            self.ui_home.password=self.password
            id=self.db.get_user_id(self.username)
            tuplaNombre=self.db.obtener_apellidos_nombres(id)
            self.ui_home.nombre=tuplaNombre[1]
            self.ui_home.apellido=tuplaNombre[0]
        # Obtener el PID actual del usuario si existe en la tabla SESION
            pid = self.db.get_user_pid(self.username)
            
            # Si el usuario tiene una sesión, elimínala
            if pid:
                self.db.delete_session(self.username)

            # Generar un nuevo PID y registrar la sesión en la tabla SESION
            new_pid = self.db.generate_pid()
            self.db.insert_session(self.username, new_pid)
            self.ui_home.pid=new_pid
        # Aquí establece self.ui_list antes de llamar a setupUi
        if self.idUser is not None:
            ui_list = self.db.listaUi(self.idUser)
            self.ui_home.ui_list = ui_list  # Establecer self.ui_list en ui_home
            self.consulta_clases()
            self.consultar_materias()
            self.consulta_grupos()
            self.ui_home.setupUi(self.home_window)

        #self.home_window.hide()
        self.home_window.show()
        self.ui_home.pushButton.clicked.connect(self.ui_home.home_button_clicked)
        self.ui_home.pushButton2.clicked.connect(self.ui_home.estudiante_button_clicked)
        self.ui_home.pushButton3.clicked.connect(self.ui_home.docente_button_clicked)
        self.ui_home.pushButton4.clicked.connect(self.ui_home.rol_button_clicked)
        self.ui_home.pushButton5.clicked.connect(self.cambio_perfil)
        self.ui_home.pushButton6.clicked.connect(self.inscribir)
        self.ui_home.pushButton7.clicked.connect(self.crear_materia)
    
    def consulta_clases(self):
        id_user = self.db.get_user_id(self.username)
        lista = self.db.get_student_groups(id_user)
        tupla_limpia = [(elemento[0].rstrip(), elemento[1].rstrip()) for elemento in lista]
        self.ui_home.clases = tupla_limpia
    
    def consultar_materias(self):
        lista = self.db.obtener_todas_las_materias()
        tupla_limpia = [(elemento[0], elemento[1].rstrip()) for elemento in lista]
        self.ui_home.materias= tupla_limpia

    def cambio_perfil(self):
        username = self.ui_home.lineEditUsername.text()
        password = self.ui_home.lineEditPassword.text()
        nombre = self.ui_home.lineEditNombre.text()
        apellido = self.ui_home.lineEditApellido.text()
        id_user = self.db.get_user_id(self.username)
        self.db.update_user(id_user, username, password, nombre, apellido)

    def consulta_grupos(self):
        id_user = self.db.get_user_id(self.username)
        lista = self.db.get_educador_grupos(id_user)
        tupla_limpia = [(elemento[0].rstrip(), elemento[1].rstrip()) for elemento in lista]
        self.ui_home.grupos = tupla_limpia
    
    def inscribir(self):
        id_user = self.db.get_user_id(self.username)
        materia= self.ui_home.lineEditInscribir.text()
        id_materia= self.db.get_materia_id(materia)
        self.db.agregar_estudiante_a_grupo(id_user,id_materia)
        self.ui_home.lineEditInscribir.clear()
    
    def crear_materia(self):
        nombre_materia=self.ui_home.lineEditCrear.text()
        self.db.insertar_materia(nombre_materia)
        self.ui_home.lineEditCrear.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
