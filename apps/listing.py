import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import mysql.connector

def app():
    # Add all your application here
    st.sidebar.subheader('Filer data Levels')
    connection = mysql.connector.connect(host='localhost',
                                          user='root',
                                         password='',db='5phcdb')

    census_tables = pd.read_sql_query("SELECT * FROM `level-1`", connection)
    prov = census_tables['lhh_prov'].unique()
    dist = census_tables['lhh_dist'].unique()

    params={
    'Province' : st.sidebar.selectbox('Province',prov),
    'District' : st.sidebar.selectbox('District', np.concatenate((np.array([0]),dist))),
    'Sector' : st.sidebar.selectbox('Sector',('Sector','Gashanda','Nyamata','Cyuve','Mururu')),
    'Cell' : st.sidebar.selectbox('Cell',('Cell','Murama','Munini','cyabingo','Gasharu')),
    'Village' : st.sidebar.selectbox('Village',('Village','Rutobotobo','Rutukura','Gafunzo','Sake')),
    'team(s)': st.sidebar.selectbox('Village',('Team','Team 1','Team 2','Team 3','Team 4'))
    }

    census_tables.set_index('case-id', inplace=True)

    #st.write('Province: ',params.get('Province'))
    
    #st.table(cc)
    if params.get('District') is not None:

        #cc = census_tables[(census_tables['lhh_prov']==params.get('Province'))]
        cc = census_tables[(census_tables['lhh_prov']==params.get('Province')) & (census_tables['lhh_dist']==params.get('District'))]
        st.table(cc)
    
    #Read selected values
    '''dis = st.write('District: ',params.get('District'))
    sec = st.write('Sector: ',params.get('Sector'))
    cel = st.write('Sector: ',params.get('Cell'))
    vil = st.write('Sector: ',params.get('Village'))
    team = st.write('Sector: ',params.get('Team'))'''