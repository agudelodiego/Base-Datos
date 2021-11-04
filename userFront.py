'''
REALIZADO POR: Diego Alexander Agudelo Garcia
DESCRIPCION: El presente archivo tiene el objetivo de diseñar un programa que interactue con el usuario haciendo uso de las funcionalidades desarrolladas en archivo userApp.py 
'''


#------------------------------------------------Importamos los modulos necesarios----------------------------------------------
from userApp import*
#-------------------------------------------------------------------------------------------------------------------------------

#*-------------------------------------------------Diseño del programa de usuario------------------------------------------------
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
#*-------------------------------------------------------------------------------------------------------------------------------