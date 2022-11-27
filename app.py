import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import datetime
from PIL import Image

st.set_page_config(layout="centered", page_title="Online Sales")
st.markdown('# Online Sales ')
st.markdown('##   ')

st.header('Online Retail Sales 2016 - 2018')
st.subheader('Linear regression chart')

df_retail = pd.read_excel('retailsales2.xlsx')
col_select = st.selectbox('Select a category', df_retail.columns[4:13], index=4)

df_retail['Date'] = pd.to_datetime(df_retail['Date'], format='%Y-%m', errors='ignore')
fig = px.scatter(df_retail, x=df_retail["2016-2018"], y=col_select, trendline="ols", title="")
st.plotly_chart(fig)

st.subheader('Bar chart')
col_chart = st.selectbox('Select a category', df_retail.columns[4:13], index=6)
fig2 = px.bar(df_retail, x='Date', y=col_chart, title="")
st.plotly_chart(fig2)

df_table = pd.read_excel('retailsales2.xlsx', usecols='D, F, G, H, I, J, K')
df_table['Date'] = pd.to_datetime(df_retail['Date'], format='%Y-%m', errors='ignore')
if st.checkbox("Show data table"):
    st.dataframe(df_table )


###########
st.markdown('#  ')
st.header('Cars Buyers')

df_buyers = pd.read_excel("carbuyers.xlsx")

choose_chart = st.selectbox('Select Pie chart or Bar chart?', ['Pie chart','Bar chart'])
if choose_chart == 'Pie chart':
    fig = px.pie(df_buyers, values='Total', names='Manufacturer')
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.plotly_chart(fig)
elif choose_chart == 'Bar chart':
    fig = px.histogram(df_buyers, x="Manufacturer", y="Total",
             color='Fuel', barmode='group')
    st.plotly_chart(fig)

st.subheader('Cars Sales data table')
text_input = st.text_input("Enter car manufacturer name")
text_lower = text_input[:3].lower()

if text_input:
    car_data = df_buyers.where(df_buyers['Manufacturer'].astype(str).str[:3].apply(lambda x: x.lower()) == text_lower)
    car_data = car_data.dropna()

    st.dataframe(car_data)

#############
st.markdown('#  ')
st.header('Total Cars Sales')

total = st.radio("Select Total Sales", ('Total Sales', 'Total Women Buyers', 'Total Men Buyers'))
if total == 'Total Sales':
    fig3 = px.histogram(df_buyers, x="Manufacturer", y="Total", barmode="group", color="Manufacturer")
    st.plotly_chart(fig3)
elif total == 'Total Women Buyers':
    fig3 = px.histogram(df_buyers, x="Manufacturer", y="Female", barmode="group", color="Manufacturer")
    st.plotly_chart(fig3)
else:
    fig3 = px.histogram(df_buyers, x="Manufacturer", y="Male", barmode="group", color="Manufacturer")
    st.plotly_chart(fig3)
