# Net Worth Forecaster

The Net Worth Forecaster is a script designed to predict future net worth based on historical values. It utilizes the Prophet library, which is an open-source tool developed by Facebook for time series forecasting.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Data Retrieval](#data-retrieval)
- [Prediction](#prediction)
- [Exploring the Forecast](#exploring-the-forecast)
- [Conclusion](#conclusion)

## Introduction

The Net Worth Forecaster analyzes historical net worth data and uses it to predict future net worth values. It visualizes the actual data, applies the forecasting model, and presents the forecasted net worth values. The script is configured to forecast net worth for the coming 5 years.

## Requirements

The following libraries are required to run the Net Worth Forecaster script:
- `prophet` - The core library for time series forecasting.
- `datetime` - Library for working with dates and times.
- `matplotlib.pyplot` - Library for creating plots and visualizations.
- `pandas` - Library for data manipulation and analysis.
- `pymysql` - Library for connecting to a MySQL database.

Ensure that these libraries are installed before using the Net Worth Forecaster script.

## Data Retrieval

The Net Worth Forecaster retrieves historical net worth data from a MySQL database. The `get_data` function connects to the database and fetches the necessary data. The query selects the date and net worth values from the `networth` table.

## Prediction

The Net Worth Forecaster applies the Prophet forecasting model to the historical net worth data. The `predict` function prepares the data for forecasting by renaming the columns to `ds` and `y`. The `prophet` object is initialized with daily and weekly seasonality disabled. The model is then fitted with the data.

A future dataframe is created using the `make_future_dataframe` method. The forecast is generated using the `prophet.predict` method. The resulting forecast data is plotted on a graph using `prophet.plot`. The x-axis represents the date, and the y-axis represents the net worth. The graph is then displayed.

The forecast itself is returned by the `predict` function.

## Exploring the Forecast

The Net Worth Forecaster provides a function called `exploreForecast` to analyze the forecasted values. It filters the forecast to include only future dates and selects columns for date, net worth, upper bound, and lower bound. These values are then indexed by date.

The function identifies specific target dates for analysis based on month and day combinations. It retrieves the forecasted net worth values for these target dates and displays them along with the current net worth, which is extracted from the last row of the historical data.

Finally, the `exploreForecast` function displays the target dates and their corresponding forecasted net worth values.
