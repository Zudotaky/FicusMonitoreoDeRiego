
import mysql.connector

"""" Estos son los comandos usados para crear la base de datos y tablas
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rootroot",database="Flores")   
    mycursor =  mydb.cursor()
    
    mycursor.execute("CREATE DATABASE dbFlores")
    mycursor.execute("CREATE TABLE Plantas (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(255),descripcion VARCHAR(255))")
    mycursor.execute("CREATE TABLE Senseo (id INT PRIMARY KEY,estado VARCHAR(255),fecha DATETIME,FOREIGN KEY(id) REFERENCES Plantas(id) )")
    
    sql = "INSERT INTO Plantas (nombre,descripcion) VALUES (%s,%s)"
    val = ("rose", "esto es una descripcion")
    mycursor.execute(sql, val)
    mydb.commit()
"""


class DaoFlor:

    queryCrearFlor = "INSERT INTO Plantas (nombre,descripcion) VALUES (%s,%s);"
    queryRecuperarFlores = "SELECT * from Plantas"
    queryGuardarSenseo = "INSERT INTO Senseo (id,estado,fecha) VALUES (%s,%s,%s);"

    def __init__(self):
        self.flores = self.obtenerPlantas()

    def obtenerPlantas(self):
        self.connectarSql()
        mycursor = self.mysqlConector.cursor()
        mycursor.execute(self.queryRecuperarFlores)
        self.flores = mycursor.fetchall()
        self.cerrarSql()
        return self.flores

    def persistirPlanta(self,Planta):
        self.connectarSql()
        mycursor = self.mysqlConector.cursor()
        mycursor.execute(self.queryCrearFlor,(Planta.nombre(),Planta.descripcion()))
        self.mysqlConector.commit()
        id = mycursor.lastrowid
        Planta.cambiarId(id)
        self.cerrarSql()

    def agregarSenseo(self, id , estadoDePlanta, fechaActual):
        datos=( id,estadoDePlanta,fechaActual)
        self.connectarSql()
        mycursor = self.mysqlConector.cursor()
        mycursor.execute(self.queryGuardarSenseo,datos)
        self.mysqlConector.commit()
        self.cerrarSql()


    def connectarSql(self):
        self.mysqlConector = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="rootroot",
            database="dbFlores")

    def cerrarSql(self):
        self.mysqlConector.close()



