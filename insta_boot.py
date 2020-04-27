from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InstaBoot:

    # recebe uma string com usuário e senha
    # Inicializa o chromedriver e maximiza a tela
    def __init__(self, usuario, senha):
        self.__user = usuario
        self.__password = senha
        self.__driver = webdriver.Chrome(executable_path=r'C:\Users\rodri\OneDrive\choemedriver\chromedriver.exe')
        self.__chorme_maximixa = webdriver.Chrome.maximize_window(self.__driver)

    def login(self):
        """ Metodo que acessa os campos de input name e password
        e enviar os valores de usuario e senha passados em InstaBoot """

        driver = self.__driver
        driver.get('https://www.instagram.com/')
        time.sleep(1)
        user_element = driver.find_element_by_xpath('//input[@name="username"]')
        user_element.click()
        user_element.clear()
        user_element.send_keys(self.__user)
        password_elemente = driver.find_element_by_xpath('//input[@name="password"]')
        password_elemente.click()
        password_elemente.clear()
        password_elemente.send_keys(self.__password)
        password_elemente.send_keys(Keys.RETURN)
        time.sleep(3)

    def curti_fotos(self, hastg):
        """ Curtir foto recebe o parametros o nome da hastag acessa a página
        e coleta os links os links da página, logo em seguida acessa cada um dos links
        e curte as as botos quando há o botão de like"""

        driver = self.__driver
        driver.get(f'https://www.instagram.com/explore/tags/{hastg}/')
        time.sleep(2)
        for i in range(1, 4):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

        print(f' fotos com as {hastg}: {str(len(pic_hrefs))}')

        for pic_hrefs in pic_hrefs:
            driver.get(pic_hrefs)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)
            try:
                like = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button')
                like.click()
                time.sleep(19)
                print('deu certo porra')

            except Exception as e:
                print('deu errado')

    def segue_sugeridos(self):
        """ Segue sugeridos clica no botão ver todos e
        clica no botão seguir continuamente"""
        
        driver = self.__driver
        time.sleep(3)
        driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")[0].click()
        time.sleep(3)
        driver.find_elements_by_link_text("Ver tudo")[1].click()

        for index in range(0, 31):
            time.sleep(3)
            driver.find_elements_by_tag_name('button')[index].click()
            print(index)
            time.sleep(10)

    def status_instaBoot(self):
        print(f'usuario: {self.__user}\n'
              f'Senha: {self.__password}')
