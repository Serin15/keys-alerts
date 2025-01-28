import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):

    BUTTON_JS_ALERT = (By.CSS_SELECTOR, "[onclick='jsAlert()']")
    BUTTON_JS_CONFIRM = (By.CSS_SELECTOR, "[onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.CSS_SELECTOR, "[onclick='jsPrompt()']")
    P_RESULT = (By.ID, "result")


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.driver.quit()


    def test_simple_alert(self):
        self.driver.find_element(*self.BUTTON_JS_ALERT).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.assertEqual(self.driver.find_element(*self.P_RESULT).text, "You successfully clicked an alert" )

    def test_dismiss_alert(self):
        self.driver.find_element(*self.BUTTON_JS_CONFIRM).click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        self.assertEqual(self.driver.find_element(*self.P_RESULT).text, "You clicked: Cancel")

    def test_prompt_alert(self):
        self.driver.find_element(*self.BUTTON_JS_PROMPT).click()

        alert = self.driver.switch_to.alert
        text = "text123"
        alert.send_keys(text)

        alert.accept()
        self.assertEqual(self.driver.find_element(*self.P_RESULT).text, f"You entered: {text}" )
