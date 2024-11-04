from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def current_url(self):
        return self.browser.current_url

    def find_element_located(self, locator, time=20):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_visibility(self, locator, timeout=20):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                          message=f'Cant find element by locator {locator}')


    def find_element_not_located(self, locator, time=10):
        WebDriverWait(self.browser, time).until(EC.invisibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    def find_element_located_click(self, locator):
        self.find_element_located(locator).click()

    def execute_script(self, locator):
        return self.browser.execute_script("arguments[0].scrollIntoView();", locator)

    def drag_and_drop(self, element_one, element_two):
        element = self.browser.find_element(*element_one)
        target = self.browser.find_element(*element_two)
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop(element, target).perform()

    def move_to_element_and_click(self, locator):
        element = self.browser.find_element(*locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).click().perform()

    def get_text(self, locator):
        element = self.find_element_visibility(locator)
        return element.text

    def get_text_locator(self, locator):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        return self.browser.find_element(*locator).text

    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.browser, 20).until(EC.presence_of_all_elements_located(locator))

    def click_element_if_clickable(self, locator):
        click_element = self.find_element_visibility(locator)
        self.browser.execute_script('arguments[0].click();', click_element)
