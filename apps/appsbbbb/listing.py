import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    # Add all your application here
    st.sidebar.subheader('View Levels')

    params={
    'Province' : st.sidebar.selectbox('Province',('Kigali city','East','West','South')),
    'District' : st.sidebar.selectbox('District',('Nyarugenge','Gasabo','Kicukiro','Burera')),
    'Sector' : st.sidebar.selectbox('Sector',('Gashanda','Nyamata','Cyuve','Mururu')),
    'Cell' : st.sidebar.selectbox('Cell',('Murama','Munini','cyabingo','Gasharu')),
    'Village' : st.sidebar.selectbox('Village',('Rutobotobo','Rutukura','Gafunzo','Sake'))

    }

