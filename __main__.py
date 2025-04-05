from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os

mtaMusicas = 'https://site.mtabrasil.com.br/musicas/';

def reload():
    os.system('cls' if os.name == 'nt' else 'clear')
    __main__();


def __main__():
    print('################################\n');
    print('MTA - Buscador de músicas \n');
    print('Desenvolvido por: yLorde \n');
    print('################################\n');

    nomeDaMusica = input('Nome da música >>  ');

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    driver.minimize_window();

    print('🌐 Abrindo navegador...')

    print('🌐 Carregando página...');
    driver.get(mtaMusicas);

    driver.find_element(By.ID, 'search_youtube').send_keys(nomeDaMusica);
    print('🔄 Buscando música...')

    driver.implicitly_wait(4);

    driver.find_element(By.ID, "btn_busca_youtube").click();
    
    primeiroElemento = driver.find_element(By.ID, "result_youtube").find_elements(By.TAG_NAME, "div")[0];
    primeiroElementoTitulo = driver.find_element(By.ID, "result_youtube").find_elements(By.TAG_NAME, "strong")[0];

    primeiroElemento.find_element(By.TAG_NAME, "button").click();

    print('🔄 Copiando link...');
    print('✅ Link da música copiada para sua área de transferência');

    driver.quit();
    reload();

if __name__ == '__main__':
    __main__();

