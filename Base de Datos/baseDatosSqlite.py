import sqlite3

# CONECTAR EN LA BD
def conectar():
    conexion = sqlite3.connect("miBD.db")
    cursor = conexion.cursor()
    return conexion, cursor


# CREAR LA TABLA agenda EN LA BD
def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            telefono VARCHAR(14) NOT NULL
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
        INSERT INTO agenda(nombre, telefono) VALUES(?,?)
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
    cursor.execute("SELECT id,nombre,telefono FROM agenda") 
    for fila in cursor:
        print("ID = ", fila[0])
        print("Nombre = ", fila[1])
        print("Telefono = ", fila[2], "\n")
    conexion.close()


# MODIFICAR DATOS EN LA BD
def modificar(id,telefono):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET TELEFONO="+telefono+" WHERE ID="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()


# ELIMINACIÓN DE UN DATO EN LA BD
def borrar(id):
    conexion, cursor = conectar()
    sql = "DELETE FROM agenda WHERE ID="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()


# Ejemplos 
crearTabla()
datos = ("Pepe", "12345678")
insertar(datos)
datos = ("Bichu", "7777777")
insertar(datos)
consultar()
modificar("1","4444444")
consultar()
borrar("1")
consultar()