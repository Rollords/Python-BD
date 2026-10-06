import mysql.connector
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password= '',
            database = 'clinica',
            port= '3306'        
            )
        print('Conexion exitosa!')
        return conexion
    except mysql.connector.Error as error:
        print(f'Algo salio mal D: {error}')
        return None
    except Exception as error :
        print('Error inesperado')
        return None

conectar = conectar_bd()