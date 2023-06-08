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

    if report == 'Balance Sheet':  # По году #######################################################################
        empty_list = [''] * len(df)
        df['TTM'] = empty_list
        df = df.iloc[:, [0, 1, 2, 3, 8, 7, 6, 5, 4]]
    else:
        df = df.iloc[:, [0, 1, 2, 3, 4, 8, 7, 6, 5]]

    df.loc[len(df) + 2] = [''] * 9

    return df


def main():
    yahoo_tickers = ['IL', 'VI', 'KL', 'CO', 'TW', 'SA', 'LS', 'BK', 'TO', 'ST', 'AX', 'MI', 'PA', 'AS', 'HK', 'MC',
                     'SN', 'DE', 'T', 'KS', 'BR', 'OL', 'SW', 'IS', 'MX', 'SS', 'AT', 'JK']
    reports = ['Income Statement', 'Balance Sheet']

    writer = pd.ExcelWriter('Yahoo.xlsx', engine='xlsxwriter')

    for ticker in yahoo_tickers:

        balance_income_list = []
        for report in reports:
            try:
                balance_income_list.append(get_data_yahoo(report, ticker))
                print(f'{ticker} {report} done!')
            except Exception as Ex:
                print(ticker, report)
                print(Ex)
                balance_income_list.append(pd.DataFrame({'Ошибка': [],	'Error': [],
                                                         'Erreur': [], 'Fehler': [], 'Errore': [],
                                                         '错误': [], 'エラー': [], '오류': [],
                                                         f'На Yahoo нет данных по {ticker}': []}))

        dataframe = pd.concat(balance_income_list)
        dataframe.to_excel(writer, sheet_name=f'{ticker}', index=False)

    writer.save()


if __name__ == '__main__':
    main()


# ME, CO в балансе 3 года
