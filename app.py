import streamlit as st
from apps.multiapp import MultiApp
from apps import home, listing, interview # import your app modules here

a,b = st.beta_columns(2)
with a:
    st.image('./img/nisr.jpg',width=200)

st.sidebar.image('./img/nisr.jpg',width=150)

with b:
    title = 'CENSUS DATA COLLECTION PROGRESS REPORT'
    st.markdown(
            f'<div class="laert alert-success" style="margin-top:0px; border:solid black; padding:5px; color: black;font-familly:Arial sans-serif; font-size: large"><b><i><center>{title}</center></i></b></div>',
            unsafe_allow_html=True)


app = MultiApp()

a,b = st.beta_columns(2)
app.add_app("Home", home.app)
app.add_app("Listing", listing.app)
app.add_app("Interview", interview.app)

app.run()