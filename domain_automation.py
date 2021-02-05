from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from ebird_api import get_bird_name

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck='

bird_list = get_bird_name()


def check_random_domain():

    n = random.randint(0, len(bird_list) - 1)
    bird_name = bird_list[n]

    search_url = url + bird_name

    driver.get(search_url)

    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[1]')))
    except:
        pass

    if 'available' in element.text:
        return search_url, bird_name

    return None, bird_name


while True:
    search_url, bird_name = check_random_domain()
    if search_url:
        print(bird_name + ".com is available. Do you want to open browser?")
        user_input = input()
        if int(user_input) == 1:
            new_driver = webdriver.Chrome()
            new_driver.get(search_url)

            driver.quit()
