#!/usr/bin/env python3

# Reference:
#https://medium.com/data-science-everywhere/linear-regression-is-simple-81a05da5e0e1
# https://www.tutorialspoint.com/scikit_learn/scikit_learn_linear_regression.htm
# https://realpython.com/linear-regression-in-python/

import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso
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

# def predict(df)

def sample():
    # Features (X)
    X = np.array([[1,2],[2,4],[3,6],[4,8]])
    # Target (y)
    y = np.array([1, 2, 3, 4]).reshape((-1, 1))

    model = LinearRegression(copy_X = True).fit(X, y)


    print(X)
    print(y)

    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    print('score:', model.score(X, y))

    y_pred = model.predict(X)
    print('predicted response:', y_pred, sep='\n')



if __name__ == '__main__':
    df = getData()
    df.columns = ['date', 'netWorth']
    df['date'] = df['date'].astype('datetime64[ns]').map(dt.datetime.toordinal)
    df['netWorth'] = df['netWorth'].astype('float')

    rows, cols = df.shape
    X = df.iloc[:,:-1].to_numpy()
    y = df.iloc[:,cols-1].to_numpy().reshape((-1,1))
    # rows, cols = df.shape
    # X = df.iloc[:,:-1]
    # y = df.iloc[:,cols-1]


    model = LinearRegression()
    model.fit(X,y)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    print('score:', model.score(X, y))
    y_pred = model.predict(X)


    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(X, y, label='Net Worth (Actuals)')
    ax.plot(X, y_pred, 'b', label='Net Worth (Prediction)')
    ax.legend(loc=2)
    ax.set_title('Net Worth')
    plt.show()
