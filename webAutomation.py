from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://wcaquino.me/cypress/componentes.html")

# campo_busca = driver.find_element(By.CSS_SELECTOR, "#formNome")
# campo_busca.send_keys("Ceciany")
# campo_busca1 = driver.find_element(By.CSS_SELECTOR, "#formSobrenome")
# campo_busca1.send_keys("Soarigues")
# sexo = driver.find_element(By.CSS_SELECTOR, "#formSexoFem")
# sexo.click()
# comidafavorita = driver.find_element(By.CSS_SELECTOR, "#formComidaPizza")
# comidafavorita.click()
# #sugestoes = driver.find_element(By.CSS_SELECTOR, "#elementosForm\\:sugestoes")
# sugestoes = driver.find_element(By.CSS_SELECTOR, 'textarea[id="elementosForm:sugestoes"]')
# sugestoes.send_keys("Nenhuma sugestão.")

# button_click_me = driver.find_element(By.CSS_SELECTOR, "#buttonSimple")
# texto_antes = button_click_me.get_attribute("value")
# print(f"Texto do botão antes do click: {texto_antes}")
# button_click_me.click()
# texto_depois = button_click_me.get_attribute("value")
# print(f"Texto do botão depois do click: {texto_depois}")

button_resposta_demorada = driver.find_element(By.CSS_SELECTOR, "#buttonDelay")
button_resposta_demorada.click()
time.sleep(5)

novocampo = driver.find_element(By.CSS_SELECTOR, "#novoCampo")
novocampo.send_keys("Novo Campo")



time.sleep(10)

driver.close()