from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT_USER = (By.XPATH, "//*[@id='username']")
    SEARCH_INPUT_PASSWORD = (By.XPATH, "//*[@id='password']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='loginbtn']")
    BUTTON_RESULT = SEARCH_BUTTON
    RESULTS = (By.XPATH, "//*[@id='action-menu-toggle-1']")
    BUTTON_LOGOUT = (By.XPATH, "//*[@id='actionmenuaction-7']")
