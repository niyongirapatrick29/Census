import streamlit as st
import mysql.connector
import pandas as pd
#import config as cf

def app():
    st.title('Home')

    st.write('This is the `home page` of this multi-page app.')

    st.write('In this app, we will be building a simple classification model using the Iris dataset.')
    connection = mysql.connector.connect(host='sql10.freemysqlhosting.net',
                                         user='sql10411482',
                                         password='VmhMnlwmuN',db='sql10411482')

    census_data = pd.read_sql_query("SHOW TABLES", connection)
    st.write(census_data)