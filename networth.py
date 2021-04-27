#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chart_studio
import chart_studio.plotly as py
import os
import pandas as pd
import plotly.express as px
import yaml

conf = yaml.load(open('config.yaml'),Loader=yaml.FullLoader)

username = conf['username']
api_key = conf['plotlyApiKey']
input_file = conf['inputFile']

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


df = pd.read_csv(input_file, 
                 parse_dates = ['Date'], 
                 index_col='Date')

fig = px.area(df,
    title='Net Worth (CAD)',
    labels={'variable':'Net Worth (CAD)',
            'value': 'Net Worth (CAD)'})
fig.update_layout(showlegend=False)
             
#fig.show()
py.plot(fig, filename = 'net_worth', auto_open=False)
