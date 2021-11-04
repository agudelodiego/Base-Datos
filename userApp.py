'''
REALIZADO POR: Diego Alexander Agudelo Garcia
DESCRIPCION: El presente archivo tiene como finalidad el diseño de una entidad, la cual contenga todos los metodos y funcionalidades necesarias para interactuar con el usuario, dicha clase se llamara usuario_APP
'''


#--------------------------------------------Importamos los modulos necesarios----------------------------------
from Loggin import*
from usuarioDTO import*
from Conexion_Pool import*
from Cursor_Conexion import*
from usuarioDAO import*
from validacionesDAO import*
import psycopg2
#---------------------------------------------------------------------------------------------------------------



#*-----------------------------------------------Creacion de la calse-------------------------------------------
class usuario_APP: 

    #----------------------------------Metodo menu------------------------------
    @classmethod
    def menu(cls):

        sms = '''
        ----------------------PROGRAMA DE USUARIO-----------------------

                                OPCIONES
            1 -> Mostrar la lista de los usuario registrados.
            2 -> Agregar un nuevo usuario.
            3 -> Actualizar un usuario ya existente.
            4 -> Eliminar un usuario.
            5 -> Salir del programa de usuario.
            6 -> Volver a mostrar este menu.
            '''
        return sms
    #---------------------------------------------------------------------------


    #----------------------------Metodo listar usuarios---------------------------
    @classmethod
    def listar(cls):

        lista = usuario_DAO().seleccionar()
        
        for i in lista:
            print(i)
    #-----------------------------------------------------------------------------


    #-------------------------------Metodo agregarUser-----------------------------
    @classmethod
    def agregarUser(cls):

        print('''
            IMPORTANTE: Si desea volver al programa principal debera introducir el comando "salir"

            Usted ha seleccionado la opcion de agregar un nuevo usuario. Para realizar dicho 
            tramite de manera exitosa debera proporcionar primeramente un nombre de usuario 
            y un email que no existan en la base de datos, asi como una contraseña, misma que sera 
            seleccionada y confirmada por usted. A continuacion debera empezar con el proceso.
        ''')

        userName = None
        email = None
        password = None
        Salir = None

        #----------------------Verificar el nombre usuario--------------------
        while (userName == None)and(Salir == None):

            userName = input('''
                POR FAVOR INGRESE EL NOMBRE DE USUARIO DESEADO
                >> ''')

            #Analizamos el dato ingresado por el suario
            if userName == 'salir':
                Salir = userName
                break

            #Verificar si el nombre de usuario existe o no dentro de la base de datos
            verificar = validacion_DAO().verificar_userName(userName)

            if verificar == True:
                print(F'''
                    El nombre de usuario "{userName}"" ya esta siendo utilizado por alguien dentro de 
                    nuestra base de datos, por favor vuelva a intentarlo
                ''')
                userName = None

            elif verificar == False:
                print(f'''
                    El nombre de usuario "{userName}" fue procesado y verificado exitosamente
                ''')
        #-----------------------------------------------------------------

        #------------------------Verificar el email-----------------------
        while (email == None)and(Salir == None):

            email = input('''
                POR FAVOR INTRODUZCA UNA DIRECCION DE CORREO ELECTRONICO
                >> ''')

            #Analizamos el email ingresado por el usuario
            if email == 'salir':
                Salir = email
                break

            #Verificar si el email esta en uso o no
            verificar = validacion_DAO().verificar_email(email)

            if verificar == True:
                print(f'''
                    El correo electronico "{email}" fue verificado y procesado correctamente,
                    puede continuar con el proceso
                ''')
            
            elif verificar == False:
                print('''
                    Correo electronico invalido, intentelo nuevamente
                ''')
                email = None
        #----------------------------------------------------------------

        #---------------------Verificar la contraseña--------------------
        while (password == None)and(Salir == None):

            password = input('''
                POR FAVOR INGRESE LA CONTRASEÑA SELECCIONADA
                >> ''')

            if password == 'salir':
                Salir = password
                break

            confirmacion = input('''
                CONFIRME SU CONTRASEÑA
                >> ''')



            if password == confirmacion:
                print('>>   Contraseña ingresada exitosamente')

            else:
                print('>>   Vuelva a intentarlo')
                password = None
        #----------------------------------------------------------------

        #-------------Insercion del usuario en la base de datos-----------
        if Salir == None:

            insertado = usuario_DAO().insertar(userName=userName, email=email, password=password)
            print(f'''
                INFORMACION INGRESADA
                El suario ha sido ingresado exitosamente

                DESCRIPCION:
            ''')
            print(insertado)
        #-------------------------------------------------------------------

        #---------------------Volviendo al programa principal---------------
        if Salir == 'salir':
            print('''
            Volviendo al programa principal, por favor espere ...
                                                              ...
                                                              ...
                                                              ...
            ''')
        #-------------------------------------------------------------------
            
    #------------------------------------------------------------------------------


    #-------------------------------Metodo actualizarUser---------------------------
    @classmethod
    def actualizarUser(cls):

        print('''
            IMPORTANTE: Si desea volver al programa principal solo debera de introducir el 
            comando salir en minusculas

            Usted ha seleccionado la opcion actulizar usuario, para realizar el tramite usted
            debera proporcionar el usuario que desea modificar, dicho usuario debe de existir 
            dentro de nuestra base de datos, una vez se verifique la existencia del usuario 
            debera de ingresar un nuevo nombre de usuario, un nuevo email y una nueva contraseña.
        ''')
        
        userName = None
        new_userName = None
        new_email = None
        new_password = None
        user_ID = None
        Salir = None

        #--------------------------Verificacion de usuario----------------------- 
        while (userName == None)and(Salir == None):

            userName = input('''
                POR FAVOR INGRESE EL NOMBRE DEL USUARIO QUE DESEA MODICAR
                >> ''')

            #Verificamos el dato ingresado por el usuario
            if userName == 'salir':
                Salir = userName
                break

            validacion = validacion_DAO().verificar_userName(userName)

            if validacion == True:
                print(f'''
                    El usuario "{userName}" fue encontrado dentro de la base de datos, puede 
                    continuar con el tramite
                ''')

            else:
                print(f'''
                    El usuario {userName} no fue encontrado en la base de datos, por favor
                    vuelva a intentarlo
                ''')
                userName = None
        #--------------------------------------------------------------------------

        #------------------------Pedir el nuevo nombre de usuario-------------------
        while (new_userName == None)and(Salir == None):

            new_userName = input('''
                INTRODUZCA EL NUEVO NOMBRE DE USUARIO
                >> ''')

            #Verificamos el dato ingresado por el usuario 
            if new_userName == 'salir':
                Salir = new_userName
                break

            #Validar si el nombre existe o no dentro de la base de datos
            validacion = validacion_DAO().verificar_userName(new_userName)

            if validacion == False:
                print('''
                    Procesando el dato introducido, por favor espere ...
                                                                     ...
                ''')

            else:
                print('''
                    Por favor vuelva a intentarlo
                ''')
                new_userName = None
        #--------------------------------------------------------------------------

        #-----------------------Pedir el nuevo correo electronico------------------
        while (new_email == None)and(Salir == None):

            new_email = input('''
                INGRESE EL NUEVO CORREO ELECTRONICO
                >> ''')

            #Verificamos el dato ingresado por el usuario 
            if new_email == 'salir':
                Salir = new_email
                break

            #Validacion de la direccion de correo electronico
            validacion = validacion_DAO().verificar_email(new_email)

            if validacion == True:
                print(f'''
                    El correo electronico "{new_email}" fue validado y procesamente, puede continuar
                    con los tramites
                ''')

            else:
                new_email = None
                print('''
                    Su direccion de correo electronico no es valida, vuelva a intentarlo
                ''')
        #----------------------------------------------------------------------------

        #--------------------------------Pedir contraseña----------------------------
        while (new_password == None)and(Salir == None):

            new_password = input('''
                ESTABLESCA UNA CONTRASELA
                >> ''')

            #Verficamos el dato ingresado por el usuario
            if new_password == 'salir':
                Salir = new_password
                break

            #Verificacion de contraseña
            comparacion = input('''
                CONFIRMAR CONTRASEÑA
                >> ''')

            if new_password == comparacion:
                print('''
                    Contrasela ingresada y procesada de manera exitosa, realizando el cambio 
                    en la base de datos, por favo respere
                ''')
            
            else:
                print('''
                    Parece que has cometido un erro al confirmar la contraseña, vuela intentarlo
                ''')
                new_password = None
        #----------------------------------------------------------------------------

        #------------------------Realizando la actualizacion del usuario-------------
        if Salir == None:

            #Solicitamos el objeto usuario que se va a actualizar 
            usuario = validacion_DAO().buscar(userName)
            user_ID = usuario.userID

            #Actualizar el usuario seleccionado
            new_usuario = usuario_DAO().actualizar(user_ID, new_userName, new_email, new_password)

            print(f'''
                ************************** USUARIO ACTUALIZADO EXITOSAMENTE **************************
                                        DESCRIPCION DE LA OPERACION REALIZADA
                
                Usuario antrior:
                {usuario}

                Nuevo usuario:
                {new_usuario}
                                                
                                                OPERACION FINALIZADA
                ****************************************************************************************
            ''')
        #----------------------------------------------------------------------------

        #------------------------Volviendo al programa principal---------------------
        if Salir == 'salir':
            print('''
                Volviendo la programa principal, por favor espere ...
                                                                  ...
                                                                  ...
            ''')
        #----------------------------------------------------------------------------
    #-------------------------------------------------------------------------------


    #---------------------------------Metodo elminarUser----------------------------
    @classmethod
    def eliminarUser(cls):

        print('''
            IMPORTANTE: Si desea volver al programa principal solo debera de introducir el 
            comando salir en minusculas

            Usted a seleccionado la opcion de eliminar un ususario, para realizar el tramite 
            debera de introducir un usuario existente dentro de la base de datos
        ''')

        userName = None
        Salir = None

        #--------------------------Pedir el nombre del usuario a eliminar-------------------
        while (userName == None)and(Salir == None):

            userName = input('''
                INGRESE EL NOMBRE DEL USUARIO QUE DESEA ELIMINAR
                >> ''')

            #Verificando el dato ingresado por el usuario 
            if userName == 'salir':
                Salir = userName
                break

            #Validar que el usuario exista
            validacion = validacion_DAO().buscar(userName)

            if validacion == None:

                print(f'''
                    El usuario "{userName}" no fue encontrado dentro de la base de datos, 
                    por favor intentelo nuevamente    
                ''')
                userName = None

            else:

                print(f'''
                    El usuario {userName} se encontro exitosamente en la base de datos
                    Descipcion: {validacion}
                ''')
        #-----------------------------------------------------------------------------------

        #----------------------------------Pedir confirmacion-------------------------------
        if Salir == None:
            print('''
                >>  IMPORTANTE: Una vez realizados los cambio no habra poder humano que logre 
                    deshacer los cambios, por favor, pienselo bien, no sea estupido y no haga
                    cosas de las que despues se puede arrepentir
            ''')

        while Salir == None:

            confirmacion = input('''
                Desea continuar con la eliminacion del usuario ?(S/N)
                >> ''')
            confirmacion = confirmacion.upper()
            
            if confirmacion == 'S':
                usuario_DAO().eliminar(validacion.userID)
                print('''
                    El usuario ha sido eliminado de la base de datos
                    ''')
                break
            
            elif confirmacion == 'N':
                print('''
                    Elinacion de usuario cancelada, volviendo al programa principal
                ''')
                break

            else:
                print('''
                    Ups, parece que has introducido una opcion no valida, vuelva a intentarlo
                    ''')
        #-----------------------------------------------------------------------------------

        #-----------------------Volviendo al programa principal-----------------------------
        if Salir == 'salir':
            print('''
                Volviendo al programa principal, por favor esepe un momento ...
                                                                            ...
                                                                            ...
            ''')
        #-----------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------
#*---------------------------------------------------------------------------------------------------------------





#!-----------------------------------------------ENTORNO DE PRUEBAS----------------------------------------------
if __name__ == '__main__':
    
    while True:

        print(usuario_APP().menu())
        opcion = input('<<  Introduzca la opcion seleccionada: ')

        if opcion == '1':
            print('         MOSTRANDO LOS USUARIO DENTRO DE LA BASE DE DATOS')
            usuario_APP().listar()
            print('FIN'.center(70,'*'))

        elif opcion == '2':
            usuario_APP().agregarUser()

        elif opcion == '3':
            usuario_APP().actualizarUser() 

        elif opcion == '4':
            usuario_APP().eliminarUser()

        elif opcion == '5':
            print('>>   Saliendo de programa de usuario, por favor espere ...')
            break

        elif opcion == '6':
            continue
#!---------------------------------------------------------------------------------------------------------------