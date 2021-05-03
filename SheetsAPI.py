import gspread
import os

__sheetName__ = 'Cupones'
__accessKey__= shAcessKey
__jsonName__ = 'credentials.json'
__jsonPath__ = os.path.dirname(os.path.abspath(__file__))
__filename__ = os.path.join(__jsonPath__, __jsonName__)

#connect to workspace
__gc__ = gspread.service_account(filename=__filename__)
__sh__ = __gc__.open_by_key(__accessKey__)
worksheet = __sh__.worksheet(__sheetName__)

nombreClientes = worksheet.get('B7:B')
codigoCupones = worksheet.get('E7:E')
