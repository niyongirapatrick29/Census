from typing import Sized
from pandas.core.indexing import is_label_like
import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np

#import config as cf

#st.beta_set_page_config(page_title='Kike.io',page_icon=":smiley:")
#st.set_page_config({"title":"Patrick"})

def app():
    
    '''connection = mysql.connector.connect(host='sql10.freemysqlhosting.net',
                                         user='sql10411482',
                                         password='VmhMnlwmuN',db='sql10411482')'''
    connection = mysql.connector.connect(host='localhost',
                                          user='root',
                                         password='',db='5phcdb')

    census_tables = pd.read_sql_query("SELECT * FROM `level-1`", connection)
    world = pd.read_csv('./covid_19_data.csv')
    districts = world['Country'].unique()

    #Progress bar of all cases
    bar = st.sidebar.progress(0)
    
    bar.progress(10)
    st.sidebar.write(world.count()['Confirmed'].astype(int))

    c = st.selectbox('',np.concatenate((np.array(['- All district -']),districts)))
    
    if c!='- All district -':
        
        st.markdown(
        f'<div class="laert alert-success" style="color: green; font-size: large"><center><b>Listing progress summary in {c} </b></center></div>',
        unsafe_allow_html=True)

        coutry_data = world[world['Country']==c]
        
        coutry_data.rename(columns = {'Lat':'lat','Long':'lon'}, inplace=True)
        st.map(coutry_data)
        st.subheader("Total Households done in  "+ c)
        st.table((coutry_data.groupby('Country')['Confirmed'].agg(['count','max']).reset_index()))

    elif c=='- All district -':
        st.markdown(
        f'<div class="laert alert-success" style="color: green; font-size: large"><center><b>Listing progress summary in all district</b></center></div>',
        unsafe_allow_html=True)

        world.rename(columns={'Lat':'lat','Long':'lon'}, inplace=True)
        #st.write(China.head(10))
        st.map(world)
        st.subheader("Table Summary information per all districts")
        st.table((world.groupby('Country')['Confirmed'].count()).reset_index())


    census_tables['lhh_dist'] = census_tables['lhh_dist'].map({11:'Nyarugenge', 31:'Nyamagabe',36:'Rusizi'}) 
    by_idst = census_tables.groupby(by='lhh_dist', as_index=True)['lhh_sect'].count()

    st.subheader("‘Progress by District")
    
    #Bar Chart
    #st.bar_chart(by_idst)

    '''#Line Chart
    st.line_chart(by_idst)
    by_idst = by_idst.reset_index()

    
    agree = st.button('Click to View cases by District')
    #Display 
    
    if agree:
        by_idst.set_index('lhh_sect', inplace=True)
        st.bar_chart(by_idst['lhh_dist'])'''

    st.markdown(
            f'<div class="laert alert-success" style="color: green; font-size: large"><center>Interview progress summary in all district</center></div>',
            unsafe_allow_html=True)
