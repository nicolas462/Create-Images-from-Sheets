import os
from PIL import Image, ImageDraw, ImageFont, ImageShow
import DropboxAPI

#def paths
__absolutePath__ = os.path.dirname(os.path.abspath(__file__))
__imgFile__ = os.path.join(__absolutePath__, 'CuponReferidoPlantilla.png')
__imgFileSaved__ = os.path.join(__absolutePath__, 'Cupon.png')
__fontFile__ = os.path.join(__absolutePath__, "CONSOLA.TTF")

#establishes font
sizeFont = 18
font = ImageFont.truetype(__fontFile__, sizeFont)

x = 286
y = 195
shadowColor = "rgb(170, 200, 255)"
textColor = "rgb(102, 134, 200)"

def generarCupon(texto, name):
    #open image
    image = Image.open(__imgFile__)
    draw = ImageDraw.Draw(image)
    #shadow
    draw.text((x,y+2),texto.upper(),font=font, fill=shadowColor)
    #text
    draw.text((x,y),texto.upper(),font=font, fill=textColor)
    
    image.save(__imgFileSaved__)
    f = open(__imgFileSaved__, 'rb')
    DropboxAPI.saveFile(f.read(), name)

def deleteFile():
    os.remove(__imgFileSaved__)
