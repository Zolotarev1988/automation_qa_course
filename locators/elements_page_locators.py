from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    #form fields
    FULL_NAME = (By.XPATH, "//input[@id ='userName']")
    EMAIL = (By.XPATH, "//input[@id ='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id ='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id ='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id ='submit']")


    #created from
    CREATED_FULL_NAME = (By.XPATH, "//p[@id ='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id ='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id ='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id ='permanentAddress']")


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title ='Expand all']")
    ITEM_LIST = (By.XPATH, "//span[@class ='rct-title']")
    CHECKED_ITEMS = (By.XPATH, "//*[@class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class RadioButtonPageLocators:

    YES_RADIOBUTTON = (By.XPATH, "//label[@class ='custom-control-label' and text()= 'Yes']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[@class ='custom-control-label' and text()= 'Impressive']")
    NO_RADIOBUTTON = (By.XPATH, "//label[contains(@class, 'custom-control-label') and text()= 'No']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")
