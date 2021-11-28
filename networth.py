#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prophet import Prophet
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from dbconnect import connection

plt.style.use('ggplot')


def getData():
    cur, conn = connection("portfolio")
    resultValue = cur.execute("SELECT * FROM networth WHERE date > (DATE_SUB(CURDATE(), INTERVAL 2 YEAR))")
    if resultValue > 0:
        data = cur.fetchall()
        df = pd.DataFrame(data)
        return df
    else:
        return "Database is empty!"


def predict(df):
    df.columns = ['ds', 'y']
    prophet = Prophet(daily_seasonality=False, weekly_seasonality=False)

    # fit data to model
    prophet.fit(df)

    # build future dataframe for 5 years
    future = prophet.make_future_dataframe(periods=5*12, freq='M')

    # make predictions
    forecast = prophet.predict(future)

    # plot forecasts
    prophet.plot(forecast, xlabel='Date', ylabel='Net Worth')
    plt.title('Net Worth Forecast')

    # tell us more about the forecast
    # prophet.plot_components(forecast)

    plt.show(block=False)

    return forecast


def exploreForecast(forecast, df):
    predict = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    predict.columns = ['date', 'net worth', 'upper bound', 'lower bound']
    output = predict.loc[predict['date'] > dt.datetime.today(),
                         ['date', 'net worth']][::6]

    print('Net worth targets (CAD) : ')
    for index, row in output.iterrows():
        print('{:%Y-%m-%d}'.format(row['date']),
              ': $'+'{:,.0f}'.format(row['net worth']))

    print('\rCurrent Net Worth: ' + '$' + '{:,.0f}'.format(df.iloc[-1, 1]))

    return None


if __name__ == '__main__':
    df = getData()
    df.columns = ['date', 'netWorth']
    df['date'] = df['date'].astype('datetime64[ns]')
    df['netWorth'] = df['netWorth'].astype('float')

    plt.figure(figsize=(8, 4))
    plt.grid(linestyle='-.')
    plt.plot(df['date'], df['netWorth'])
    plt.show(block=False)

    forecast = predict(df)

    exploreForecast(forecast, df)

    plt.show()
