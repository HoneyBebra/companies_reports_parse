import pandas as pd

from classes import Yahoo


def main():
    yahoo_tickers = ['DE', 'T', 'KS', 'SS', 'ME', 'HK', 'TW', 'JK', 'TO', 'IS', 'CO', 'KL', 'PA', 'SA', 'BK', 'SW',
                     'MX', 'L', 'SN', 'OL', 'ST', 'SW', 'VI', 'MI', 'IL', 'AT', 'MC', 'LS', 'AX', 'ME', 'AS', 'DE',
                     'BR', 'TO']

    yahoo_income = Yahoo(report='Balance Sheet')
    url = yahoo_income.get_url('DE')

    name_ticker = yahoo_income.get_company_name(url)
    name = ' '.join(name_ticker.split()[:-1])
    ticker = ''.join(name_ticker.split()[-1])

    head = yahoo_income.get_head(url)

    all_data = yahoo_income.get_all_data(url)
    df = pd.DataFrame({name: [''], ticker: ['']})
    for col_name in head:
        df[col_name] = ['']

    for i in range(3, len(all_data) + 3):
        df.loc[i] = ['', ''] + all_data[i - 3]

    df.to_excel('/Users/pavelseryi/PycharmProjects/pythonProject/balance_parser/Выгрузка тест.xlsx',
                index=False)

    # Поменять столбцы местами
    # Убрать 2 пустую строку


if __name__ == '__main__':
    main()
