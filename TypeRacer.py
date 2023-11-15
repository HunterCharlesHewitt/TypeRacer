from pynput.keyboard import Controller
from time import sleep

from selenium.webdriver.common.by import By


class TypeRacer:
    def __init__(self, web_driver):
        self.seconds_to_hold_key_down = 0.01
        self.seconds_between_key_presses = 0.095
        self.seconds_to_sleep_after_entering_race = 15
        self.seconds_to_sleep_after_landing_page = 2
        self.seconds_to_sleep_until_collecting_html = 1
        self.driver = web_driver
    def click_enter_typing_race(self):
        sleep(self.seconds_to_sleep_after_landing_page)
        element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Enter a Typing Race')]")
        element.click()
        sleep(self.seconds_to_sleep_until_collecting_html)

    def format_text_to_type(self, texts):
        combined_text = ' '.join(texts)
        if len(texts[0]) == 1:
            combined_text = combined_text[:1] + combined_text[2:]
        return combined_text
    def press_key_with_delay(self, ch, delay):
        Controller().press(ch)
        sleep(delay)
        Controller().release(ch)
    def type_characters(self):
        texts = [e.text for e in self.driver.find_elements(By.XPATH, "//span[@unselectable='on']")]
        formatted_texts = self.format_text_to_type(texts)
        sleep(self.seconds_to_sleep_after_entering_race)
        for ch in formatted_texts:
            self.press_key_with_delay(ch, self.seconds_to_hold_key_down)
            sleep(self.seconds_between_key_presses)

    def do_single_race(self):
        self.click_enter_typing_race()
        self.type_characters()
        sleep(5)

