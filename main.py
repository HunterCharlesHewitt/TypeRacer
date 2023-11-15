from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from TypeRacer import TypeRacer


def get_webdriver_with_url(web_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get(web_url)
    return driver


if __name__ == '__main__':
    driver = get_webdriver_with_url("https://typeracer.com")
    type_racer = TypeRacer(driver)
    type_racer.do_single_race()
