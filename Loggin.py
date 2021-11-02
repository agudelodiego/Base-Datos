#--------------------IMPORTAMOS MODULOS NECESARIOS---------------------
import logging as log
#----------------------------------------------------------------------



#------------------CONFIGURACION DEL OBJETO LOG------------------------
log.basicConfig(
    format='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s',
    level=log.INFO,
    datefmt='%I:%M:%S %p ',
    handlers=[
        log.FileHandler('Proyectos/Proyecto3/registros.log'),
        log.StreamHandler()
    ]
)
#-----------------------------------------------------------------------



#!----------------------PRUEBAS DE FUNCIONAMIENTO-----------------------
if __name__ == '__main__':
    
    log.debug('Esto es una prueba')
#!---------------------------------------------------------------------