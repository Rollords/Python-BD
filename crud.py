from conex import conectar_bd
import _mysql_connector

def leer_registro(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM paciente")
    resultados= cursor.fetchall()
    for pacientes in resultados:
        print(pacientes)
    cursor.close()

conexion = conectar_bd()

if conexion:
    leer_registro(conexion)
    conexion.close()
    