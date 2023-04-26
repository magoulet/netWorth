#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prophet import Prophet
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
# import yaml
import pymysql

plt.style.use('ggplot')


def get_data():
    # Connect to the database
    db = pymysql.connect(host="raspberrypi1", port=3306, user="admin", password="password", database="portfolio")

    # Fetch data from the networth table
    query = "SELECT date, netWorthUsd FROM networth"
    df = pd.read_sql(query, db)
    # Convert the 'date' column to datetime and set as index
    # df["date"] = pd.to_datetime(df["date"])
    # df.set_index("date", inplace=True)
    return df

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

    predict = predict.loc[predict['date'] > dt.datetime.today(),['date', 'net worth']]

    predict.set_index('date', inplace=True)

    target_dates = predict.index[(predict.index.month == 6) & (predict.index.day == 30) | (predict.index.month == 12) & (predict.index.day == 31)]

    for target_date in target_dates:
        net_worth_target = predict.loc[target_date]["net worth"]
        print(f"{target_date.strftime('%Y-%m-%d')}: ${net_worth_target:,.0f}")

    print('\rCurrent Net Worth: ' + '$' + '{:,.0f}'.format(df.iloc[-1, 1]))

    return None


if __name__ == '__main__':
    df = get_data()

    # Plot the results
    plt.plot(df.date, df['netWorthUsd'], label='Actual')
    plt.legend()
    plt.show(block=False)

    forecast = predict(df)

    exploreForecast(forecast, df)

    plt.show()
