""" 
	Hecho por: Alejandro Mendez Astudillo
	Descripcion: Este script lee todas las lineas de un fichero y las imprime en pantalla
"""

import sys
import os.path

def getLinesFile( _path ):
    if ( not os.path.isfile( _path ) ):
        print( "El fichero no se localiza o no existe" )
        sys.exit( )
    file_r = open( _path, 'r' )
    list_lines = file_r.readlines( )
    file_r.close( )
    return list_lines 

def printList( _list ):
    for item in _list:
        print( item )

def createAndWrite(path, list_lines):
	_file = open(path, "w")
	for line in list_lines:
		_file.write(line)
	_file.close()	

if __name__ == "__main__":
    if len( sys.argv ) == 2:
        lines = getLinesFile( sys.argv[ 1 ] )
        printList( lines )
    else:
        print( "Se debe ingresar como parametro el nombre del fichero a leer con su respectiva ruta, ya sea absoluta o relativa" )
