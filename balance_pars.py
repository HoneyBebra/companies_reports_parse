import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
import requests
from bs4 import BeautifulSoup as BS
# from selenium.webdriver.chrome.service import Service


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


def main():
    yahoo_tickers = ['DE', 'T', 'KS', 'SS', 'ME', 'HK', 'TW', 'JK', 'TO', 'IS', 'CO', 'KL', 'PA', 'SA', 'BK', 'SW',
                     'MX', 'L', 'SN', 'OL', 'ST', 'SW', 'VI', 'MI', 'IL', 'AT', 'MC', 'LS', 'AX', 'ME', 'AS', 'DE',
                     'BR', 'TO']

    yahoo_income = Yahoo(report='Income Statement')
    url = yahoo_income.get_url('GM')
    print(url)


if __name__ == '__main__':
    main()
