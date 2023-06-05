from classes import Yahoo


def main():
    yahoo_tickers = ['DE', 'T', 'KS', 'SS', 'ME', 'HK', 'TW', 'JK', 'TO', 'IS', 'CO', 'KL', 'PA', 'SA', 'BK', 'SW',
                     'MX', 'L', 'SN', 'OL', 'ST', 'SW', 'VI', 'MI', 'IL', 'AT', 'MC', 'LS', 'AX', 'ME', 'AS', 'DE',
                     'BR', 'TO']

    yahoo_income = Yahoo(report='Income Statement')
    url = yahoo_income.get_url('GM')
    print(yahoo_income.get_company_name(url))


if __name__ == '__main__':
    main()
