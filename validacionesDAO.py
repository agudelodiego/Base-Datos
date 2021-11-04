'''
REALIZADO POR: Diego Alexander Agudelo Garcia
DESCROPCION: El presente archivo tiene el objetivo de servile a la capa de aplicacion como interfas para realizar validaciones de usuario, lo cual se lograma mediante una clase llamada validaciones_DAO, misma que contendra todos los metodos necesarios para cumplir con el ojetivo
'''


#------------------------------------------------Importamos los modulos necesarios----------------------------------------------
from Loggin import*
from usuarioDTO import*
from Conexion_Pool import*
from Cursor_Conexion import*
from usuarioDAO import*
import psycopg2
#-------------------------------------------------------------------------------------------------------------------------------




#*--------------------------------------------------Creacion de la calse---------------------------------------------------------
class validacion_DAO:

    #--------------------------------------Metodo valdiar userName---------------------------------
    @classmethod
    def verificar_userName(cls,valor):

        validacion = usuario_DAO().seleccionar()

        for i in validacion:

            flag = False

            if valor == i.userName:
                print(f'''
                    El nombre de usuario "{valor}" ya esta siendo utilizado por otro usuario
                    dentro de la aplicacion
                ''')
                flag = True
                break

        return flag
    #----------------------------------------------------------------------------------------------


    #---------------------------------------Metodo verificar email---------------------------------
    @classmethod
    def verificar_email(cls,valor):

        setencia_1 = ('@gmail.com' in valor)or('@hotmail.com' in valor)or('@mail.com' in valor)
        setencia_2 = True

        if setencia_1 == False:
            print(f'''
                El correo electronico ingresado tiene una extension invalida.
                IMPORTANTE: Los correos elctronicos deben de contar una extension valida, como por 
                ejemplo @mail.com, @hotmail.com, @gmail.com, entre otros.
            ''')

        validacion = usuario_DAO().seleccionar()

        for i in validacion:

            if valor == i.email:
                print(f'''
                    El correo electronico "{valor}" ya esta siendo utilizado por un usuario dentro de la 
                    base de datos
                ''')
                setencia_2 = False
                break
        
        if (setencia_1)and(setencia_2):
            log.info('Correo electrnico procesado y validado correctamente, puede continuar con el proceso')
            return True
        else:
            log.info('Correo electronico invalido')
            return False
    #----------------------------------------------------------------------------------------------



    #---------------------------------------Metodo buscar usuario----------------------------------
    @classmethod
    def buscar(cls,user):

        usuariosBD = usuario_DAO().seleccionar()
        usuarioEncontrado = None

        #Iteramos la lista para hallar al usuario
        for i in usuariosBD:

            if user == i.userName:
                usuarioEncontrado = i

        return usuarioEncontrado
    #----------------------------------------------------------------------------------------------
#*-------------------------------------------------------------------------------------------------------------------------------




#!-----------------------------------------------------------ENTORNO DE PRUEBAS--------------------------------------------------
if __name__ == '__main__':  

    '''La verificacion del nombre de usuario o userNaeme se encarga de verificar si un determinado nombre de usuario exites o no dentro la base de datos. Funciona de la siguiente manera:
    
        variable = validacion_DAO().verificar_userName(nombre)
        
    Dicho metodo devuelve True si el nombre existe dentro de la base de datos, y devuelve False si el nombre no existe dentro de la base de datos'''
    ejemplo_1 = validacion_DAO().verificar_userName('HolaMundo')
    print(ejemplo_1)



    
    '''La verificacion de emil se encarga de verificar si un determinado correo electronico es valido o no, para tomor dicha desicion realiza dos validaciones, la primera es validar que la direccion de correo electronico sea un direccion valida, es decir, que tenga @mail.com, o @gmail.com, o @hotmail.com
    
        variable = validacion_DAO().verificar_email(email)
        
    Dicho metodo devuelve True si el email es valido, y devuelve False si el email es invalido'''
    ejemplo_2 = validacion_DAO().verificar_email('ajajaaj@mail.com')
    print(ejemplo_2)



    '''La busqueda de un usuario dentro de la base de datos, se realiza con el metodo validacion_DAO().buscar(userName), dicho metodo retorna None en caso de no haber encontrado al usuario, y retorna el objeto usuario en caso de coincidencias'''
    ejemplo_3 = validacion_DAO().buscar('HolaMundo')
    print(ejemplo_3)
#!-------------------------------------------------------------------------------------------------------------------------------