#------------------Importamos los modulos necesarios------------------
import psycopg2
from psycopg2 import pool
from Loggin import log
import sys
from Conexion_Pool import*
from usuarioDTO import*
#---------------------------------------------------------------------



#*-----------------------------------Creacion de la clase cursor-------------------------------------
class Cursor_Conexion:

    #-----------------------------Metodo constructor-------------------------
    def __init__(self):
        self._conn = None
        self._curss = None
    #------------------------------------------------------------------------


    #---------------------------------Metodo enter---------------------------
    def __enter__(self):
        self._conn = Conexion_Pool.get_conexion() 
        log.debug(f'''
            *******************************Descripcion de conexion*********************************
            OBJETO: {self._conn}
            TIPO: {type(self._conn)}
        ''')
        self._curss = self._conn.cursor()
        log.debug(f'''
            *******************************Descripcion del cursor**********************************
            OBJETO: {self._curss}
            TIPO: {type(self._curss)}
        ''')
        return self._curss
    #------------------------------------------------------------------------


    #---------------------------------Metodo exit-----------------------------
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        if valor_excepcion:
            self._conn.rollback()
            log.error(f'''
                            PARECE QUE ALGO HA MALIDO SAL
                descripcion: {detalle_excepcion}
                tipo: {tipo_excepcion}
                valor: {valor_excepcion}
            ''')
            
        else:
            self._conn.commit()
            log.debug('''
                OPERACION REALIZADA DE MANERA EXITOSA
            ''')
            self._curss.close()
            log.debug('''
                CRUSOR CERRADO EXITOSAMENTE
            ''')
            Conexion_Pool.close_conexion(self._conn)
    #-------------------------------------------------------------------------
#*---------------------------------------------------------------------------------------------------



#!--------------------------------------ENTORNO DE PRUEBAS-------------------------------------------
if __name__ == '__main__':

    #--------------------------Invocamos al context manager------------------------
    with Cursor_Conexion() as cursor:

        #Creacion del objeto
        usuario_X = usuario_DTO(userID=1, userName='HolaMundo', email='HolaGoogle@espias.putos', password='5678')

        #Definimos la query que deseamos realizar
        query = 'INSERT INTO "usuarios_info"("userName","email","password") VALUES(%s,%s,%s)'

        #Introducimos los valores en un tupla
        valores = (usuario_X.userName, usuario_X.email, usuario_X.password)

        #Ejecutamos la query
        cursor.execute(query, valores)

        #Capturamos la respuesta
        insertados = cursor.rowcount


        #Mostramos la respuesta
        log.info(f'''
        Registros insertados :: {insertados}
        Objeto insertado :: {usuario_X}
        ''')
    #---------------------------------------------------------------------------------
#!---------------------------------------------------------------------------------------------------
