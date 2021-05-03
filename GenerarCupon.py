#import DropboxAPI
import PillowAPI
import SheetsAPI

def generar():
    for (i, item) in enumerate(SheetsAPI.nombreClientes, start=0):
        #parse to string
        name = ''.join(item)
        code = ''.join(SheetsAPI.codigoCupones[i])

        nameFile = name+' - '+code+'.png'
        PillowAPI.generarCupon(code, nameFile)
        PillowAPI.deleteFile()