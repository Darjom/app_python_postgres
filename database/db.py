import psycopg2

class DatabaseManager:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        if not self.connection or self.connection.closed != 0:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            )

    def close(self):
        if self.connection:
            self.connection.close()

    def insert_user(self, username, password):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO USERN (username, password) VALUES (%s, %s)", (username, password))
        self.connection.commit()
        cursor.close()

    def get_user_id(self, username):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID_USERN FROM USERN WHERE username = %s", (username,))
        user_id = cursor.fetchone()
        cursor.close()
        if user_id:
            return user_id[0]
        else:
            return None

    def verify_credentials(self, username, password):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM USERN WHERE username = %s AND password = %s", (username, password))
        count = cursor.fetchone()[0]
        cursor.close()
        
        return count == 1
    
    def generate_pid(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT pg_backend_pid();")
        new_pid = cursor.fetchone()[0]
        cursor.close()
        return new_pid

    def get_user_pid(self, username):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT PID FROM SESION WHERE ID_USERN = (SELECT ID_USERN FROM USERN WHERE USERNAME = %s)", (username,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]  # Devuelve el PID si existe
        return None  # Retorna None si no hay sesión
    
    def obtener_apellidos_nombres(self, id_usuario):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT apellido, nombre FROM USERN WHERE ID_USERN = %s", (id_usuario,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    
    def update_user(self, user_id, new_username, new_password, new_name, new_lastname):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("UPDATE USERN SET username = %s, password = %s, nombre = %s, apellido = %s WHERE ID_USERN = %s", (new_username, new_password, new_name, new_lastname, user_id))
        self.connection.commit()
        cursor.close()

    def delete_session(self, username):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM SESION WHERE ID_USERN = (SELECT ID_USERN FROM USERN WHERE USERNAME = %s)", (username,))
        self.connection.commit()
        cursor.close()

    def insert_session(self, username, pid):
        self.connect()
        cursor = self.connection.cursor()
        user_id = self.get_user_id(username)
        if user_id is not None:
            cursor.execute("INSERT INTO SESION (ID_USERN, PID, ACTIVO) VALUES (%s, %s, %s)", (user_id, pid,True))
            self.connection.commit()
        cursor.close()

    def listaUi(self, user_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT UF.ID_UI
            FROM USERN AS U
            INNER JOIN USERN_ROL AS UR ON U.ID_USERN = UR.ID_USERN
            INNER JOIN UI_FUNCION AS UF ON UR.ID_ROL = UF.ID_FUNCION
            WHERE U.ID_USERN = %s;
        """, (user_id,))
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def get_student_groups(self, student_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT G.NOMBRE_GRUPO, M.NOMBRE_MATERIA
            FROM GRUPOS AS G
            JOIN MATERIA AS M ON G.ID_MATERIA = M.ID_MATERIA
            JOIN ESTUDIANTE_GRUPO AS EG ON G.ID_GRUPO = EG.ID_GRUPO
            WHERE EG.ID_ESTUDIANTE = %s;
        """, (student_id,))
        group_info = cursor.fetchall()
        cursor.close()
        return group_info
    
    def register_user_as_student(self, user_id, codigoEst):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO ESTUDIANTE (ID_ESTUDIANTE, CODIGO, CARRERA) VALUES (%s, %s, %s)", (user_id, codigoEst, ''))
        self.connection.commit()
        cursor.close()

    def register_user_as_teacher(self, user_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO EDUCADOR (ID_EDUCADOR, PROFESION, ESPECIALIDAD) VALUES (%s, %s, %s)", (user_id, '', ''))
        self.connection.commit()
        cursor.close()

    def get_educador_grupos(self, educador_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT G.NOMBRE_GRUPO, M.NOMBRE_MATERIA
        FROM GRUPOS AS G
        INNER JOIN EDUCADOR_GRUPO AS EG ON G.ID_GRUPO = EG.ID_GRUPO
        INNER JOIN MATERIA AS M ON G.ID_MATERIA = M.ID_MATERIA
        WHERE EG.ID_EDUCADOR = %s;
        """, (educador_id,))
        grupos = cursor.fetchall()
        cursor.close()
        return grupos


    def get_materia_id(self, nombre_materia):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID_MATERIA FROM MATERIA WHERE NOMBRE_MATERIA = %s", (nombre_materia,))
        materia_id = cursor.fetchone()
        cursor.close()
        if materia_id:
            return materia_id[0]  # Devuelve el ID de la materia
        return None  # Retorna None si no se encontró la materia

    def agregar_estudiante_a_grupo(self, user_id, materia_id):
        self.connect()
        cursor = self.connection.cursor()

    # Consulta para obtener el ID del grupo existente para la materia
        cursor.execute("SELECT ID_GRUPO FROM GRUPOS WHERE ID_MATERIA = %s", (materia_id,))
        grupo_id = cursor.fetchone()

        if grupo_id:
            # Si se encontró un grupo existente, usa ese ID para agregar al estudiante al grupo
            grupo_id = grupo_id[0]
            cursor.execute("INSERT INTO ESTUDIANTE_GRUPO (ID_ESTUDIANTE, ID_GRUPO) VALUES (%s, %s)", (user_id, grupo_id))
            self.connection.commit()
            cursor.close()
            return grupo_id
        else:
            cursor.close()
            return None  # Retorna None si no se encontró un grupo existente para la materia

    def insertar_materia(self, nombre_materia):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO MATERIA (NOMBRE_MATERIA) VALUES (%s)", (nombre_materia,))
        self.connection.commit()
        cursor.close()


    def obtener_todas_las_materias(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID_MATERIA, NOMBRE_MATERIA FROM MATERIA")
        materias = cursor.fetchall()
        cursor.close()
        return materias



    def close_connection(self):
        self.close()

