from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

url = 'https://wikipedia.com'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

search_language = driver.find_element_by_id('searchLanguage')
Select(search_language).select_by_visible_text('Latina')

search_textinput = driver.find_element_by_id('searchInput')
search_textinput.send_keys('Marcus Aurelius')


search_button = driver.find_element_by_xpath(
    '/html/body/div[3]/form/fieldset/button'
)
search_button.click()

print(driver.current_url)

paragraphs = driver.find_elements_by_tag_name('p')
intro_paragraph_text = paragraphs[4].text
print(intro_paragraph_text)

driver.quit()
