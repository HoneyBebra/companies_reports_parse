from selenium import webdriver
from selenium.webdriver.common.by import By


class Yahoo:

    def __init__(self, report):
        self.report = report

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(
            r'/Users/pavelseryi/PycharmProjects/pythonProject/Price_pars/chromedriver', options=options)

    def get_url(self, ticker):
        report_type = {'Income Statement': 'financials',
                       'Balance Sheet': 'balance-sheet'}

        url = f'https://finance.yahoo.com/quote/{ticker}/{report_type[self.report]}?p={ticker}'
        return url

    def get_company_name(self, url):
        driver = self.driver
        driver.get(url)
        return driver.find_element(By.ID, 'quote-header-info').text.split('\n')[0]
