'''
REALIZADO POR: Diego Alexander Agudelo Garcia
DESCRIPCION: Este archivo fue creado con el fin de servir como implementacion del patron de diseño DAO(Data Acces Objet), dicho archivo tiene la responsabilidad de ser quien realice todas las consultas SQL, asi como trabajar conjuntamente con la capa de usuario_DTO. Para lograr dicho objetivo se creara una clase llamada usuario_DAO, la cual tendra varios metodos de clase con los que la capa del programa de usuario se debera comunicar para poder realizar las operaciones sobre la base de datos
'''


#-------------------------------------------------Importamos los modulos necesarios----------------------------------------------
from Loggin import*
from usuarioDTO import*
from Conexion_Pool import*
from Cursor_Conexion import*
import psycopg2
#---------------------------------------------------------------------------------------------------------------------------------


#*-----------------------------------------------Creacion de la clase usuario_DAO-------------------------------------------------
class usuario_DAO:

    #------------------------Atributos de clase----------------------
    _SELECCIONAR = 'SELECT * FROM "usuarios_info" ORDER BY "userID"'
    _INSERTAR = 'INSERT INTO "usuarios_info"("userName","email","password") VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE "usuarios_info" SET "userName"=%s,"email"=%s,"password"=%s WHERE "userID"=%s'
    _ELIMINAR = 'DELETE FROM "usuarios_info" WHERE "userID"=%s'
    #----------------------------------------------------------------


    #-------------------------Metodo selecciona----------------------
    @classmethod
    def seleccionar(cls):

        with Cursor_Conexion() as cursor:

            cursor.execute(cls._SELECCIONAR)
            respuesta = cursor.fetchall()
            personas_BD = []

            for i in respuesta:
                pesona_X = usuario_DTO(userID=i[0], userName=i[1], email=i[2], password=i[3])
                personas_BD.append(pesona_X)
                log.debug(pesona_X)
            
            return personas_BD
    #----------------------------------------------------------------


    #--------------------------Metodo insertar-----------------------
    @classmethod
    def insertar(cls, userName, email, password):

        with Cursor_Conexion() as cursor:

            persona_X = usuario_DTO(userName=userName, email=email, password=password)
            valores = (userName,email,password)
            cursor.execute(cls._INSERTAR, valores)
            nuevo = cursor.rowcount

            log.debug(f'''
                        REGISTRO INSERTADO CON EXITO
                Registros insertados: {nuevo}
                Registro insertado: {persona_X}
                Tipo de objeto: {type(persona_X)}                
            ''')

            return persona_X
    #----------------------------------------------------------------


    #-------------------------Metodo actualizar----------------------
    @classmethod
    def actualizar(cls, userID, userName, email, password):

        with Cursor_Conexion() as cursor:

            persona_X = usuario_DTO(userID=userID, userName=userName, email=email, password=password)
            valores = (userName, email, password, userID)
            cursor.execute(cls._ACTUALIZAR, valores)
            actualizados = cursor.rowcount

            log.debug(f'''
                        REGISTRO ACTUALIZADO CORRECTAMENTE
                Registros actualizados: {actualizados}
                Registro introducido: {persona_X}
            ''')

            return persona_X
    #----------------------------------------------------------------


    #---------------------------Metodo eliminar----------------------
    @classmethod
    def eliminar(cls, userID):

        with Cursor_Conexion() as cursor:

            valores = (userID,)
            cursor.execute(cls._ELIMINAR, valores)
            eliminados = cursor.rowcount

            log.info(f'''
                    REGISTRO ELIMINADO EXITOSAMENTE
                Registros eliminados: {eliminados}
            ''')
    #----------------------------------------------------------------
#*-----------------------------------------------------------------------------------------------------------------------------------



#!------------------------------------------------------ENTORNO DE PRUEBAS-----------------------------------------------------------
if __name__ == '__main__':

    #------------------------Prueba metodo seleccionar------------------------
    seleccion1 = usuario_DAO().seleccionar()
    for i in seleccion1:
        log.info(f'''
            Descripcion del registro
            {i}
        ''')
    #-------------------------------------------------------------------------


    #-------------------------Prueba metodo insertar--------------------------
    insercion1 = usuario_DAO().insertar('XmanY','Ywomen@mail.com','29179')
    log.info(f'''
                    OBJETO INSERTADO EN LA BASE DE DATOS
        Descripcion: {insercion1}
    ''')
    #-------------------------------------------------------------------------


    #--------------------------Prueba metodo actualizar-----------------------
    actualizacon1 = usuario_DAO().actualizar(3,'PutoMan','elPuto@mail.putis','puercas')
    log.info(f'''
                ACTUALIZACION EXITOSA   
        Descripcion: {actualizacon1}
    ''')
    #-------------------------------------------------------------------------


    #---------------------------Prueba metodo eliminar------------------------
    usuario_DAO().eliminar(1)
    #-------------------------------------------------------------------------
#!-----------------------------------------------------------------------------------------------------------------------------------