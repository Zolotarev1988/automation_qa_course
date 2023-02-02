from selenium.webdriver.support.ui import  WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)


    def element_is_visible(self, locator, timout=5):  #element_is_visible в следующий раз использовать его
        return wait(self.driver, timout).until(EC.visibility_of_element_located(locator))  #Жди какое то время пока не найдется нужный элемент

    def elements_are_visible(self, locator, timout=5):
        return wait(self.driver, timout).until(EC.visibility_of_all_elements_located(locator)) #видно все элементы

    def element_is_present(self, locator, timout=5):
        return wait(self.driver, timout).until(EC.presence_of_element_located(locator)) # Когда не видно элемент но он есть в доме дерева

    def elements_are_present(self, locator, timout=5):
        return wait(self.driver, timout).until(EC.presence_of_all_elements_located(locator)) # # Когда не видно элементЫ но они есть в доме дерева

    def element_is_not_visible(self, locator, timout=5):
        return wait(self.driver, timout).until(EC.invisibility_of_element_located(locator)) # не видимый элемент

    def element_is_clickable(self, locator, timout=5):
        return wait(self.driver, timout).until(EC.element_to_be_clickable(locator)) # кликабелность элемент

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element) # перемещает, скролит сразу к нужному элементу