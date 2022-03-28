import sqlite3

# CONECTAR EN LA BD
def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    return conexion, cursor


# CREAR LA TABLA agenda EN LA BD
def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            apellido VARCHAR(20) NOT NULL,
            telefono VARCHAR(14) NOT NULL,
            email VARCHAR(20) NOT NULL
        )
    """
    if cursor.execute(sql):
        print("Tabla creada.")
    else:
        print("No se pudo crear la tabla.")
    conexion.close()


# INSERTAR DATOS EN UNA BD
def insertar(datos):
    conexion, cursor = conectar()
    sql = """
        INSERT INTO agenda(nombre, apellido, telefono, email) VALUES(?,?,?,?)
    """ 
    if cursor.execute(sql, datos):
        print("Datos insertados.")
    else:
        print("No se pudieron insertar los datos.")  
    conexion.commit() 
    conexion.close()
    

# CONSULTAR EN LA BD
def consultar():
    conexion, cursor = conectar()
    sql = "SELECT id,nombre,apellido,telefono,email FROM agenda"
    cursor.execute(sql) 
    listado = []
    for fila in cursor:
        listado.append(fila)
    #     print("ID = ", fila[0])
    #     print("Nombre = ", fila[1])
    #     print("Apellido: ", fila[2])
    #     print("Telefono = ", fila[3])
    #     print("Email = ", fila[4], "\n")
    listado.sort()
    conexion.close()
    return listado

# CONSULTAR POR ID
def consultarXid(id):
    conexion, cursor = conectar()
    sql = "SELECT * FROM agenda WHERE id="+str(id)
    cursor.execute(sql)
    contacto = cursor.fetchall()
    conexion.close()
    return contacto

# MODIFICAR DATOS EN LA BD
def modificar(id,nombre,apellido,telefono,email):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET nombre='"+nombre+"', apellido='"+apellido+"', telefono='"+telefono+"', email='"+email+"' WHERE id="+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()


# ELIMINACIÓN DE UN DATO EN LA BD
def borrar(id):
    conexion, cursor = conectar()
    sql = "DELETE FROM agenda WHERE id="+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()