from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# Asi que crearemos un objeto que haga que deje el explorador
# abierto una vez que se terminen las pruebas
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get("https://github.com")
link = browser.find_element(By.CLASS_NAME, "Button-label")
link.click()
alink = browser.find_element(By.LINK_TEXT, "Sign in")
alink.click()
# Si compilamos lo abrirá pero lo cerrará al instante por la versión que estamos usando
# de selenium
user_input = browser.find_element(By.ID, "login_field")
password_input = browser.find_element(By.ID, "password")
user_input.send_keys("jacosochoa290@outlook.com")
password_input.send_keys("isaac8alope")
password_input.send_keys(Keys.RETURN)   # Damos enter al ingresar la info

profile = browser.find_element(
    By.CLASS_NAME,
    "css-truncate.css-truncate-target.ml-1"
    # Forma para que seleccione un elemento que tenga más de una clase de cc
)
label = profile.get_attribute("innerHTML")

assert "jacob" in label  # Para indicarle si existe en esta etiqueta html
