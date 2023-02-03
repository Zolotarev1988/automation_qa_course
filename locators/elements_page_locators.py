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


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[text()='Submit']")

    # table
    FULL_PEOPLE_lIST = (By.XPATH, "//div[@class='rt-tr-group']")
    SEARCH_INPUT = (By.XPATH, "//input[@id = 'searchBox']")
    DELETE_BUTTON = (By.XPATH, "//span[@title = 'Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.XPATH, "//div[@class ='rt-noData']")
    COUNT_ROW_LIST = (By.XPATH, "//select[@aria-label ='rows per page']")

    #update
    UPDATE_BUTTON = (By.XPATH, "//span[@title='Edit']")


