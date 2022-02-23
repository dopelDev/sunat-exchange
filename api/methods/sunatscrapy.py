from requests import get
from bs4 import BeautifulSoup


def get_rate():
    URL = 'http://www.sunat.gob.pe/a/txt/tipoCambio.txt'
    html = get(URL, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})
    chunk = html.text
    date, compra, venta, _ = chunk.split('|', maxsplit=3)

    return date, compra, venta
