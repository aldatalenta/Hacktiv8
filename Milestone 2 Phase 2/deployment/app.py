import streamlit as st
import Home
import prediction

navigation = st.sidebar.selectbox('Select Page : ', ('Home', 'Predict Non and Biodegradable Material'))

if navigation == 'Home':
    Home.run()
else:
    prediction.run()