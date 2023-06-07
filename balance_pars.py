import pandas as pd
import xlsxwriter

from classes import Yahoo


def get_data_yahoo(report, ticker):
    yahoo_income = Yahoo(report=report)
    url = yahoo_income.get_url(ticker)

    name_ticker = yahoo_income.get_company_name(url)
    name = ' '.join(name_ticker.split()[:-1])
    ticker = ''.join(name_ticker.split()[-1])

    head = yahoo_income.get_head(url)

    all_data = yahoo_income.get_all_data(url)
    df = pd.DataFrame({name: [''], ticker: [''], 'Тип отчёта': [report]})
    for col_name in head:
        df[col_name] = ['']

    for i in range(3, len(all_data) + 3):
        df.loc[i] = ['', '', ''] + all_data[i - 3]

    if report == 'Balance Sheet':
        empty_list = [''] * len(df)
        df['TTM'] = empty_list
        df = df.iloc[:, [0, 1, 2, 3, 8, 7, 6, 5, 4]]
    else:
        df = df.iloc[:, [0, 1, 2, 3, 4, 8, 7, 6, 5]]

    df.loc[len(df) + 2] = [''] * 9

    return df


def main():
    yahoo_tickers = ['DE', 'T', 'KS', 'SS', 'ME', 'HK', 'TW', 'JK', 'TO', 'IS', 'CO', 'KL', 'PA', 'SA', 'BK', 'SW',
                     'MX', 'L', 'SN', 'OL', 'ST', 'SW', 'VI', 'MI', 'IL', 'AT', 'MC', 'LS', 'AX', 'ME', 'AS', 'DE',
                     'BR', 'TO']
    reports = ['Income Statement', 'Balance Sheet']

    writer = pd.ExcelWriter('Yahoo.xlsx', engine='xlsxwriter')

    i = 0
    for ticker in yahoo_tickers:

        balance_income_list = []
        for report in reports:
            try:
                balance_income_list.append(get_data_yahoo(report, ticker))
                i += 1
                print(i)
            except Exception as Ex:
                print(ticker, report)
                print(Ex)
                balance_income_list.append(pd.DataFrame({'Deere & Company': [],	'(DE)': [],	'Тип отчёта': [],
                                                         'Breakdown': [], 'TTM': [], '10/30/2019': [],
                                                         '10/30/2020': [], '10/30/2021': [], '10/30/2022': []}))

        dataframe = pd.concat(balance_income_list)
        dataframe.to_excel(writer, sheet_name=f'{ticker}', index=False)

    writer.save()


if __name__ == '__main__':
    main()


# ME в балансе 3 года
