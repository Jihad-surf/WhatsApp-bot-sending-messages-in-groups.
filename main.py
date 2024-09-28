import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller

# Importando a base de dados
df = pd.read_csv('envio_wpp/grupos.csv')
grupos  = df['Coluna1'].unique()

#chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
for grupo in grupos:
    driver.get(grupo)
    time.sleep(15)

