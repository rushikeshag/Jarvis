import webbrowser
from selenium import webdriver


def getSearch(input):
    if 'youtube'.casefold() in input.casefold():
        url = "https://www.youtube.com/"
    if 'google'.casefold() in input:
        url = "http://www.google.com/"
    if 'play song' in input:
        url = "https://youtu.be/pAgnJDJN4VA"
    webbrowser.open_new_tab(url)


class Google:
    def __init__(self):
        self.deiver = webdriver.Chrome(executable_path='D:\Code-Base\Python\chromedriver_win32\chromedriver.exe')

    def search(self, query):
        self.query = query
        self.deiver.get(url='https://www.google.com')
        search = self.deiver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(query)
        enter = self.deiver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        enter.click()

