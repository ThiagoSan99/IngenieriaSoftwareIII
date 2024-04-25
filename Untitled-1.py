from acceso import *

contenido = 'hierba'
bd = Conexion()
cursor = bd.conexion.cursor()
consulta = "SELECT * FROM Table_Recetas WHERE LOWER(Nombre) LIKE ? or LOWER(Afecciones) LIKE ? or LOWER(Ingredientes) LIKE ? or LOWER(Preparacion) LIKE ? or LOWER(Contradicciones) LIKE ?"
cursor.execute(consulta, ('%' + contenido + '%','%' + contenido + '%','%' + contenido + '%','%' + contenido + '%','%' + contenido + '%'))
table_rece = cursor.fetchall()
if len(table_rece) != 0:
    for x in range (len(table_rece)):
        print(table_rece[x][0])
else:
    print('sobelo')