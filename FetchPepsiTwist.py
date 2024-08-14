from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getPepsiTwistPrice(website : str, by : str, value : str) -> str:
    driver = webdriver.Chrome()
    driver.get(website)
    price = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((by, value))
    )
    return price.text

websiteDisco = 'https://www.disco.com.ar/gaseosa-pepsi-black-twist-354-cc/p'
websiteCoto = 'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-twist-black-pepsi-354ml/_/A-00579143-00579143-200'
websiteCarrefour = 'https://www.carrefour.com.ar/gaseosa-cola-black-pepsi-twist-en-lata-354-cc-734363/p'
websiteYaguar = 'https://shop.yaguar.com.ar/frontendSP/asp/home.asp?utm_source=acceso_directo&utm_medium=pagina_web&utm_campaign=organico&utm_term=pagina_principal&utm_content=pagina_principal'


priceCoto = getPepsiTwistPrice(websiteCoto, By.XPATH, '//*[@id="productInfoContainer"]/div/div[3]/span[2]/span')
priceCarrefour = getPepsiTwistPrice(websiteCarrefour, By.CLASS_NAME, 'valtech-carrefourar-product-price-0-x-sellingPriceValue')
priceDisco = getPepsiTwistPrice(websiteDisco, By.ID, 'priceContainer')

print(f'Precio en Coto: {priceCoto}')

print(f'Precio en Carrefour: {priceCarrefour}')

print(f'Precio en Disco: {priceDisco}')