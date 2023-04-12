import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Select Page : ', ('EDA', 'Predict Product Taken'))

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()