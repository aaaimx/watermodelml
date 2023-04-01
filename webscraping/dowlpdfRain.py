import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura la ruta del controlador del navegador
chromedriver_path = 'ruta/al/chromedriver.exe' # Reemplaza esta ruta por la tuya

# Configura las opciones del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Ejecuta el navegador en modo sin cabeza (sin interfaz gráfica)
chrome_options.add_argument('--disable-gpu')  # Desactiva la aceleración por hardware

# Crea una instancia del navegador
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Navega hasta la página web
url = 'https://example.com'
driver.get(url)

# Encuentra el botón de opciones y haz clic en él
boton_opciones = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_del_boton_de_opciones')))
boton_opciones.click()

# Encuentra las opciones y guárdalas en una lista
opciones = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@id="id_de_la_lista_de_opciones"]/li/a')))
opciones_texto = [opcion.text for opcion in opciones]

# Recorre las opciones y selecciona cada una
for opcion in opciones:
    # Selecciona la opción y espera a que cambie el contenido de la página
    opcion.click()
    time.sleep(5)  # Espera 5 segundos para que cargue el contenido
