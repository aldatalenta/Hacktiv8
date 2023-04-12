import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='Customer Churn',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Customer Churn Prediction')

    # Membuat Sub Header
    st.subheader('EDA for Customer Churn Dataset Analysis')

    # Menambahkan Gambar
    image = Image.open('churn.png')
    st.image(image, caption='Customer Churn')

    # Menambahkan Deskripsi
    st.write('This page was created by **Alda Nesti Talenta Pakpahan**')
    st.write('# Description')

    # Magic Syntax
    '''
    Customer churn rate is the percentage of customers who stop using a product in a business in a certain quarter. The percentage of lost customers affects the growth rate of the company. A high churn rate can have a negative impact on *Monthly Recurring Revenue (MRR)* and can also indicate dissatisfaction with a product. So this churn rate is an important thing that must be considered and even now it is the main reason for **PT Telco** to reduce the customer churn rate.

    In this case, the Marketing Division in this company wants to implement strategies that are relevant to the characteristics of customers who have the potential to churn so that these strategies can be right on target so as not to waste a lot of time, effort and money.

    Therefore, I'm as a Data Scientist in this company, was asked to find out the characteristics of customers who are likely to churn, namely customers who stop using the products we offer. By studying customer data such as demographic data, product ownership data and others and building a good model, companies can predict customers who will churn and take preventive measures so that these customers do not stop using the company's products.

    On this page, the author will do a simple exploration.
    The dataset used is the ***churn*** dataset.
    '''

    # Membuat Garis Lurus
    st.markdown('---')

    # Show DataFrame
    data = pd.read_csv('churn.csv')
    st.dataframe(data)

    # Observe imbalance data
    st.write('#### Distribution of Churn Risk Score')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x="churn_risk_score", data=data)
    plt.title("Churn Risk Score")
    st.pyplot(fig)

    # distribution of data from the 'churn_risk_score'/ target column
    st.write('#### Pie Plot of Churn Risk Score')
    fig = plt.figure(figsize=(7,5))
    data['churn_risk_score'].value_counts().plot(kind='pie',labels = ['',''], autopct='%1.1f%%', colors = ['indigo','salmon'], explode = [0,0.05], textprops = {"fontsize":15})
    plt.legend(labels=['Yes', 'No'])
    st.pyplot(fig)

    # Replace negative value to missing value
    data['days_since_last_login'] = data['days_since_last_login'].where(lambda x: x > 0, np.nan)

    # Membuat Violin Plot Berdasarkan Input User
    st.write('#### Violin Plot based on User Input')
    pilihan = st.selectbox('Select column : ', ('age', 'days_since_last_login', 'avg_time_spent', 'avg_transaction_value', 'avg_frequency_login_days', 'points_in_wallet'))
    fig = plt.figure(figsize=(15, 5))
    sns.violinplot(data[pilihan], palette = 'Accent', split = True)
    st.pyplot(fig)


    # plot categorical features Berdasarkan Input User
    st.write('#### Hist Plot based on User Input')
    pilihan = st.selectbox('Select column : ', ('gender', 'region_category', 'membership_category', 'joined_through_referral', 'preferred_offer_types', 'medium_of_operation', 'used_special_discount', 'offer_application_preference', 'past_complaint', 'complaint_status', 'feedback'))
    fig = plt.figure(figsize=(15, 5))
    sns.barplot(data=data, x=pilihan, y='points_in_wallet', hue = 'internet_option')
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('#### Plotly Plot - Average Transaction Value vs Churn Risk Score')
    fig = px.scatter(data, x='avg_frequency_login_days', y='churn_risk_score', hover_data=['membership_category', 'preferred_offer_types', 'avg_transaction_value', 'points_in_wallet'])
    st.plotly_chart(fig)

if __name__=='__app__':
    run()


