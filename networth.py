#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px
import chart_studio
import chart_studio.plotly as py

username = 'magoulet' # your username
api_key = 'BwgUtD4nmlTdxmP6M27k' # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


df = pd.read_csv('NetWorth.csv', 
                 parse_dates = ['Date'], 
                 index_col='Date')

fig = px.area(df,
    title='Net Worth (CAD)',
    labels={'variable':'Net Worth (CAD)',
            'value': 'Net Worth (CAD)'})
fig.update_layout(showlegend=False)
             
#fig.show()
py.plot(fig, filename = 'net_worth', auto_open=False)
