'''
REALIZADO POR: Diego Alexander Agudelo Garcia

Archivo dedicado a la implementacion del DTO(data transfer objet) de la aplicacion. Su responsabilidad es la de servirle a la aplicacion como una capa de abstraccion, la cual se encargara de manejar los usuarios de la aplicacion en forma de entidad(objetos) los cuales podran ser agregados, actualizados, leidos o eliminados de una base de datos creada mediante postgreSQL. Este archivo contendra una clase llamada usuario_DTO, la cual tendra los siguientes atributos de clase:

    - id_user -> Identificador del usuario dentro de la aplicacion
    - user_name -> Nombre del usuario dentro de la aplicacion
    - email -> Correo electronico con que el usuario se registro
    - password -> Contraseña creada por el usuario 

Responsabilidades de la clase: Crear objetos de tipo usuario
'''


#--------------------------------IMPORTAMOS LOS MODULOS NECEARIOS-------------------------------
from Loggin import*
#-----------------------------------------------------------------------------------------------



#*-------------------------------------CREACION DE LA CLASE--------------------------------------
class usuario_DTO:

    #----------------------------Constructor------------------------
    def __init__(self, userID=None, userName=None, email=None, password=None):
        self._userID=userID
        self._userName=userName
        self._email=email
        self._password=password
    #---------------------------------------------------------------


    #-----------------------Set y Get para userID-------------------
    @property
    def userID(self):
        return self._userID

    @userID.setter
    def userID(self,nuevo):
        self._userID=nuevo
    #---------------------------------------------------------------


    #----------------------Set y Get para userName------------------
    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self,nuevo):
        self._userName=nuevo
    #---------------------------------------------------------------


    #---------------------Set y Get para email----------------------
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,nuevo):
        self._email=nuevo
    #---------------------------------------------------------------

    
    #--------------------Set y Get para password--------------------
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,nuevo):
        self._password=nuevo 
    #---------------------------------------------------------------


    #--------------------------Metodo str---------------------------
    def __str__(self):
        sms = f'''
                OBJETO USUARIO CREDO EXITOSAMENTE
            user id :: {self._userID}
            user name :: {self._userName}
            email :: {self._email}
            password :: {self._password}
        '''
        return sms
    #---------------------------------------------------------------
#*-----------------------------------------------------------------------------------------------



#!-----------------------------------PRUEBAS DEL LA CLASE----------------------------------------
if __name__ == '__main__':
    
    #------------------------INSTANCIAR LA CLASE--------------------
    usuario_X0 = usuario_DTO(userID=23, userName='Prueba1', email='ejemplo1@mail.com',password='1234') 
    #---------------------------------------------------------------

    #------------------Metodos Set y Get para userID-----------------
    log.debug(f'User ID -> {usuario_X0.userID}')
    log.debug('Cambiando el ID ...')
    usuario_X0.userID = 30
    #----------------------------------------------------------------


    #----------------Metodos Set y Get para userName-------------------
    log.debug(f' userName -> {usuario_X0.userName} ')
    log.debug('Cambiando el valor de userName ...')
    usuario_X0.userName = 'elMataSuegrasSengan'
    #-----------------------------------------------------------------


    #-----------------Metodos Set y Get para email--------------------
    log.debug(f'email -> {usuario_X0.email}')
    log.debug('Cambiando el valor d email ...')
    usuario_X0.email = 'elMataSuegrasSengan@naruto.kun'
    #-----------------------------------------------------------------


    #-----------------Metodos Set y Get para password-----------------
    log.debug(f'password -> {usuario_X0.password}')
    log.debug('Cambiando el valor de password ...')
    usuario_X0.password = '5678'
    #-----------------------------------------------------------------


    #----------------------------Metodo srt---------------------------
    log.debug(usuario_X0)
    #-----------------------------------------------------------------
#!-----------------------------------------------------------------------------------------------