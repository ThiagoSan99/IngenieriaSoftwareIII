import sqlite3

class Conexion():
    def __init__(self):
        self.conexion = sqlite3.connect('Base_usuarios.db')
        

    def ingresarUsuario(self, Nombre, Codigo, UserName, Contraseña, Telefono, Correo):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Usuarios (Nombre, Codigo, UserName, Contraseña, Telefono, Correo)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(Nombre, Codigo, UserName, Contraseña, Telefono, Correo)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def busca_correo(self, id):
        cursor = self.conexion.cursor()
        bd = '''SELECT Correo FROM Usuarios WHERE Correo = ?'''
        cursor.execute(bd, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        
        if resultado:
            # Si se encontró un usuario, retornar el valor específico (en este caso, el nombre de usuario)
            return resultado
              # Retorna el primer valor de la fila
        else:
            # Si no se encontró ningún usuario, retornar None
            return None
    
    def busca_usuario(self, id):
        cursor = self.conexion.cursor()
        bd = '''SELECT UserName FROM Usuarios WHERE UserName = ?'''
        cursor.execute(bd, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        
        if resultado:
            # Si se encontró un usuario, retornar el valor específico (en este caso, el nombre de usuario)
            return resultado
              # Retorna el primer valor de la fila
        else:
            # Si no se encontró ningún usuario, retornar None
            return None
    
    def busca_contraseña(self, id):
        cursor = self.conexion.cursor()
        bd = '''SELECT Contraseña FROM Usuarios WHERE Contraseña = ?'''
        cursor.execute(bd, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            # Si se encontró un usuario, retornar el valor específico (en este caso, el nombre de usuario)
            return resultado  # Retorna el primer valor de la fila
        else:
            # Si no se encontró ningún usuario, retornar None
            return None
    
    def busca_codigo(self, id):
        cursor = self.conexion.cursor()
        bd = '''SELECT Codigo FROM Usuarios WHERE Codigo = ?'''
        cursor.execute(bd, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            # Si se encontró un usuario, retornar el valor específico (en este caso, el nombre de usuario)
            return resultado  # Retorna el primer valor de la fila
        else:
            # Si no se encontró ningún usuario, retornar None
            return None    
    
    def actualizar_nombre(self, nombre, id):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Usuarios SET Nombre = ?
                WHERE UserName = ?'''
        cursor.execute(bd, (nombre, id))
        self.conexion.commit()
        cursor.close()
    
    def actualizar_telefono(self, telefono, id):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Usuarios SET Telefono = ?
                WHERE UserName = ?'''
        cursor.execute(bd, (telefono, id))
        self.conexion.commit()
        cursor.close()
    
    def actualizar_correo(self, correo, id):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Usuarios SET Correo = ?
                WHERE UserName = ?'''
        cursor.execute(bd, (correo, id))
        self.conexion.commit()
        cursor.close()
    
    def actualizar_contraseña(self, contra, id):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Usuarios SET Contraseña = ?
                WHERE UserName = ?'''
        cursor.execute(bd, (contra, id))
        self.conexion.commit()
        cursor.close()

    def ingresarProveedor(self, Nombre, Info, Direccion, Telefono, Correo, Id_Provedor):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Table_Proovedores (Nombre, Info, Direccion, Telefono, Correo, Id_Provedor)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(Nombre, Info, Direccion, Telefono, Correo, Id_Provedor)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def busca_prov(self, id):
        cursor = self.conexion.cursor()
        bd = '''SELECT Id_Provedor FROM Table_Proovedores WHERE Id_Provedor = ?'''
        cursor.execute(bd, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            # Si se encontró un usuario, retornar el valor específico (en este caso, el nombre de usuario)
            return resultado  # Retorna el primer valor de la fila
        else:
            # Si no se encontró ningún usuario, retornar None
            return None

    def ingresarReceta(self, Nombre, Id_Receta, Afecciones, Ingredientes, Preparacion, Contradicciones, Calificacion, Dir_img):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Table_Recetas (Nombre, Id_Receta, Afecciones, Ingredientes, Preparacion, Contradicciones,  Calificacion,Dir_img)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Nombre, Id_Receta, Afecciones, Ingredientes, Preparacion, Contradicciones, Calificacion , Dir_img)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def busca_receta(self, id):
        cursor = self.conexion.cursor()
        bd = '''SELECT Id_Receta FROM Table_Recetas WHERE Id_Receta = ?'''
        cursor.execute(bd, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            # Si se encontró un usuario, retornar el valor específico (en este caso, el nombre de usuario)
            return resultado  # Retorna el primer valor de la fila
        else:
            # Si no se encontró ningún usuario, retornar None
            return None

    def ingresarRecurso(self,Num_Recurso, Id_Recurso, Nombre_Comun, Nombre_Cientifico, Descripcion, Usos, Contradicciones, Dir_Imagen):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Table_Recursos (Num_Recurso, Id_Recurso, Nombre_Comun, Nombre_Cientifico, Descripcion, Usos, Contradicciones, Dir_Imagen)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Num_Recurso, Id_Recurso, Nombre_Comun, Nombre_Cientifico, Descripcion, Usos, Contradicciones, Dir_Imagen)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def busca_recurso(self, id):
        cursor = self.conexion.cursor()
        bd = '''SELECT Id_Recurso FROM Table_Recursos WHERE Id_Recurso = ?'''
        cursor.execute(bd, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            # Si se encontró un usuario, retornar el valor específico (en este caso, el nombre de usuario)
            return resultado  # Retorna el primer valor de la fila
        else:
            # Si no se encontró ningún usuario, retornar None
            return None
    
    def actualizar_recurso(self, correo, id):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Table_Recursos SET Correo = ?
                WHERE UserName = ?'''
        cursor.execute(bd, (correo, id))
        self.conexion.commit()
        cursor.close()
    
    def generar_calificacion_receta(self, id_usu, nom_usu,id_rece, nom_rece, calificacion ):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO  Calificacion_Rece (Cod_Usuario, Nom_Usuario, Id_Receta, Nom_Receta, Calificacion)
        VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(id_usu, nom_usu,id_rece, nom_rece, calificacion)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def ingresarHistorial(self, Cod, Info, Fecha, Hora):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Historial_Usu (Cod_Usu, Contenido, Fecha, Hora)
        VALUES('{}', '{}', '{}', '{}')'''.format(Cod, Info, Fecha, Hora)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()