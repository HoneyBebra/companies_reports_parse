from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


class Yahoo:

    def __init__(self, report):
        self.report = report
        self.url_check = {}

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(
            r'C:\Users\Daniil Romanenko\PycharmProjects\pythonProject1\Pars\Price_Pars\chromedriver.exe',
            options=options)

    def get_url(self, ticker):
        report_type = {'Income Statement': 'financials',
                       'Balance Sheet': 'balance-sheet'}

        url = f'https://finance.yahoo.com/quote/{ticker}/{report_type[self.report]}?p={ticker}'
        return url

    def get_company_name(self, url):
        self.driver.get(url)
        self.url_check[url] = True
        return self.driver.find_element(By.ID, 'quote-header-info').text.split('\n')[0]

    def get_head(self, url):
        try:
            check = self.url_check[url]
            del check
        except KeyError:
            self.driver.get(url)

        report_type = {'Income Statement': 5,
                       'Balance Sheet': 4}

        head = ['Breakdown']
        for col_name in self.driver.find_elements(By.CLASS_NAME, 'BdB')[:report_type[self.report]]:
            head.append(col_name.text)

        return head

    def get_all_data(self, url):
        try:
            check = self.url_check[url]
            del check
        except KeyError:
            self.driver.get(url)

        time.sleep(random.uniform(0.5, 1))
        self.driver.find_element(By.CLASS_NAME, 'expandPf').click()

        report_type = {'Income Statement': 5,
                       'Balance Sheet': 4}

        data = []
        for row in self.driver.find_elements(By.CLASS_NAME, 'fi-row'):
            names = [' '.join(row.text.split()[:-report_type[self.report]])]
            nums = []

            for num in row.text.replace(',', '').split()[-report_type[self.report]:]:
                try:
                    nums.append(float(num))
                except ValueError:
                    nums.append(num)

            data.append(names + nums)

        return data
