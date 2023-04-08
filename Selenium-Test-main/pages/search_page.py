from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import SearchPageLocators


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://plataformavirtual.itla.edu.do/"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        # ENTRO A LA PAGINA
        self.go_to_page(self.url)

    def make_a_login_fail(self, input_user, input_password):

        # COLOCO MI USUARIO
        self.driver.find_element(
            *self.locator.SEARCH_INPUT_USER).send_keys(input_user)

        # COLOCO MI CLAVE
        self.driver.find_element(
            *self.locator.SEARCH_INPUT_PASSWORD).send_keys(input_password)

        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()

        self.wait.until(EC.presence_of_element_located(
            self.locator.BUTTON_RESULT))

        # CAPTURO IMAGEN DE SALIDA
        self.driver.save_screenshot("results/fail_login.png")

    def make_a_login_pass(self, input_user, input_password):
        self.driver.save_screenshot("results/intro_page.png")
        # COLOCO MI USUARIO
        self.driver.find_element(
            *self.locator.SEARCH_INPUT_USER).send_keys(input_user)

        self.driver.save_screenshot("results/inser_user.png")
        # COLOCO MI CLAVE

        self.driver.find_element(
            *self.locator.SEARCH_INPUT_PASSWORD).send_keys(input_password)
        self.driver.save_screenshot("results/password.png")

        # PRESIONO EL BOTON
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        self.driver.save_screenshot("results/login.png")

        # PRESIONO EL DROP LIST
        self.driver.find_element(*self.locator.RESULTS).click()
        self.driver.save_screenshot("results/droplist.png")

        # Aqui espero que apareca en DOM el id de el buton logout
        self.wait.until(EC.presence_of_element_located(
            self.locator.BUTTON_LOGOUT))
        # PRESIONO EL LOGOUT
        self.driver.find_element(*self.locator.BUTTON_LOGOUT).click()

        # CAPTURO IMAGEN DE SALIDA
        self.driver.save_screenshot("results/logut.png")
