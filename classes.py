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
            r'C:\Users\seriy_pv\PycharmProjects\pythonProject\Price_Pars\chromedriver.exe',
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
            if '/' in col_name.text or col_name.text == 'TTM':
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

        data = []
        for row in self.driver.find_elements(By.CLASS_NAME, 'fi-row'):
            names = ''
            for name in row.text.split():
                if any(str(digit) in name for digit in range(10)) or name == '-':
                    continue
                else:
                    names += name + ' '

            nums = []
            for num in row.text.replace(',', '').split():
                if any(str(digit) in num for digit in range(10)) or num == '-':
                    try:
                        nums.append(float(num))
                    except ValueError:
                        nums.append(num)

            data.append([names[:-1]] + nums)

        return data
