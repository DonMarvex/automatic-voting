from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class LoadDriver():
    def __init__(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.chrome_browser = webdriver.Chrome(service=service)
        self.chrome_browser.maximize_window()


    def voting_bot(self):
        self.chrome_browser.get('https://www.mercurynews.com/2022/01/31/vote-now-bay-area-news-group-girls-athlete-of-the-week-29/')
        time.sleep(2)
        self.chrome_browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        button_click = self.chrome_browser.find_element(By.ID, "PDI_answer50654327")
        button_click.click()
        time.sleep(2)
        vote_click = self.chrome_browser.find_element(By.ID, "pd-vote-button11033591")
        vote_click.click()
        time.sleep(5)
        return_to_poll = self.chrome_browser.find_element(By.CLASS_NAME, "pds-return-poll")
        return_to_poll.click()
        time.sleep(5)
        self.chrome_browser.close()


while True:
    bot = LoadDriver()
    bot.voting_bot()



# wait 2 seconds
# time.sleep(2)

# simulate a page scroll
# chrome_browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(10)

# show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'css-radiobutton pds-radiobutton')
# print(show_message_button.get_attribute('innerHTML'))

# button_click = chrome_browser.find_element(By.ID, "PDI_answer50654327")
# button_click.click()
# time.sleep(2)

# vote_click = chrome_browser.find_element(By.ID, "pd-vote-button11033591")
# vote_click.click()
# time.sleep(10)

# return_to_poll = chrome_browser.find_element(By.CLASS_NAME, "pds-return-poll")
# return_to_poll.click()
# time.sleep(5)

# automatically close browser window
# chrome_browser.close()

# or put entire code in a while loop to keep voting? lol
