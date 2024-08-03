from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Enviar teclas epeciais
from selenium.webdriver.support.ui import Select # Manipular dropdown
from selenium.webdriver.common.alert import Alert # Manipular alerts
from selenium.webdriver.support.ui import WebDriverWait # Gerenciando esperas
from selenium.webdriver.support import expected_conditions as EC # Gerenciando esperas
import time
import pytest

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome()
    driver.get ("https://wcaquino.me/cypress/componentes.html")
    yield driver
    driver.quit
    
def test_botao_click_me(setup_teardown):
    driver = setup_teardown
    # driver = webdriver.Chrome()
    # driver.get ("https://wcaquino.me/cypress/componentes.html")

    botao = driver.find_element (By.CSS_SELECTOR, "#buttonSimple")

    texto_antes = botao.get_attribute("value")

    assert texto_antes == "Clique Me!"

    botao.click()

    assert botao.get_attribute("value") == "Obrigado!"

    time.sleep(4)

def test_preencer_campo_nome(setup_teardown):
    driver = setup_teardown
    # driver = webdriver.Chrome()

    # driver.get ("https://wcaquino.me/cypress/componentes.html")

    campo_nome = driver.find_element (By.CSS_SELECTOR,"#formNome")

    campo_nome.send_keys("Ceciany")

    time.sleep(3)

    assert campo_nome.get_attribute ("value") == "Ceciany"

def test_checkbox (setup_teardown):
    driver = setup_teardown

    checkbox_pizza = driver.find_element (By.CSS_SELECTOR,"#FormComidaPizza")

    checkbox_pizza.click()

    assert checkbox_pizza.is_selected() == True

def test_radio_button (setup_teardown):
    driver = setup_teardown

    radio_button_sexo_masc = driver.find_element (By.CSS_SELECTOR,"#formSexoMasc")

    radio_button_sexo_masc.click()

    assert radio_button_sexo_masc.is_selected() == True