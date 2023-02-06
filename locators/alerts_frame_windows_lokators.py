from selenium.webdriver.common.by import By


class BrowserWindowsPageLokatoes:
    NEW_TAB_BUTTON = (By.XPATH, "//button[@id = 'tabButton']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id = 'windowButton']")

    TITLE_NEW = (By.XPATH, "//h1[@id = 'sampleHeading']")