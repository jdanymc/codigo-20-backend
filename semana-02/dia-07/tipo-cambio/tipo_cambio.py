import requests
from bs4 import BeautifulSoup

class TipoCambioSunat:

    def __init__(self) -> None:
        self.url = requests.get('https://www.sunat.gob.pe/')

    def optener_tipo_cambio(self):
        if(self.url.status_code==200):
            html = BeautifulSoup(self.url.text, 'html.parser')
            tipo_cambio_venta = html.find('strong',{'id':'sell-rate'})
            print(f'El tipo de cambio de venta es: {tipo_cambio_venta.get_text()}')
        else:
            print('Error al optener el tipo de cambio')

class TipoCambioSBS:

    def __init__(self) -> None:
        self.url = requests.get('https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx')

    def optener_tipo_cambio(self):
        if(self.url.status_code==200):
            html = BeautifulSoup(self.url.text, 'html.parser')
            tipo_cambio_venta = html.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__0'})
            compra = tipo_cambio_venta.find('td',{'class':'APLI_fila2'})
            print('compra : '+compra.get_text())       
        else:
            print('Error al optener el tipo de cambio')

#sunat = TipoCambioSunat()
#sunat.optener_tipo_cambio()

sbs = TipoCambioSBS()
sbs.optener_tipo_cambio()