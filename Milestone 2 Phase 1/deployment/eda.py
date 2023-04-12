import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='Travel-Package',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Holiday Package Prediction')

    # Membuat Sub Header
    st.subheader('EDA for Travel-Package Dataset Analysis')

    # Menambahkan Gambar
    image = Image.open('travel-package.jpg')
    st.image(image, caption='Travel Package')

    # Menambahkan Deskripsi
    st.write('This page was created by **Alda Nesti Talenta Pakpahan**')
    st.write('# Description')

    # Magic Syntax
    '''
    **"Trips & Travel.Com"** company wants to enable and establish a viable business model to expand the customer base. One of the ways to expand the customer base is to introduce a new offering of packages. Currently, there are 5 types of packages the company is offering - Basic, Standard, Deluxe, Super Deluxe, King. Looking at the data of the last year, we observed that 18% of the customers purchased the packages. However, the marketing cost was quite high because customers were contacted at random without looking at the available information. The company is now planning to launch a new product i.e. Wellness Tourism Package. Wellness Tourism is defined as Travel that allows the traveler to maintain, enhance or kick-start a healthy lifestyle, and support or increase one's sense of well-being. However, this time company wants to harness the available data of existing and potential customers to make the marketing expenditure more efficient.

    On this page, the author will do a simple exploration.
    The dataset used is the ***travel-package*** dataset.
    This dataset comes from **Kaggle**.
    '''

    # Membuat Garis Lurus
    st.markdown('---')

    # Show DataFrame
    data = pd.read_csv('Travel.csv')
    st.dataframe(data)

    # Observe imbalance data
    st.write('#### Distribution of Product Taken')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x="ProdTaken", data=data)
    plt.title("ProdTaken")
    st.pyplot(fig)

    # distribution of data from the 'prodtaken'/ target column
    st.write('#### Pie Plot of Product Taken')
    fig = plt.figure(figsize=(7,5))
    data['ProdTaken'].value_counts().plot(kind='pie',labels = ['',''], autopct='%1.1f%%', colors = ['indigo','salmon'], explode = [0,0.05], textprops = {"fontsize":15})
    plt.legend(labels=['No', 'Yes'])
    st.pyplot(fig)

    # Membuat Violin Plot Berdasarkan Input User
    st.write('#### Violin Plot based on User Input')
    pilihan = st.selectbox('Select column : ', ('Age', 'DurationOfPitch', 'NumberOfPersonVisiting', 'NumberOfFollowups', 'PreferredPropertyStar', 'NumberOfTrips', 'PitchSatisfactionScore', 'NumberOfChildrenVisiting', 'MonthlyIncome'))
    fig = plt.figure(figsize=(15, 5))
    sns.violinplot(data[pilihan], palette = 'Accent', split = True)
    st.pyplot(fig)

    # Replace space in value --> ' ' to ''  
    data['Gender'] = data['Gender'].str.replace(' ', '').str.capitalize()

    # plot categorical features Berdasarkan Input User
    st.write('#### Hist Plot based on User Input')
    pilihan = st.selectbox('Select column : ', ('TypeofContact', 'Occupation', 'Gender', 'ProductPitched', 'MaritalStatus', 'Designation', 'CityTier', 'Passport', 'OwnCar'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data[pilihan], palette = 'crest')
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('#### Plotly Plot - Age vs Product Taken')
    fig = px.scatter(data, x='Age', y='ProdTaken', hover_data=['PreferredPropertyStar', 'MonthlyIncome', 'CityTier', 'Occupation', 'ProductPitched', 'MaritalStatus', 'Passport', 'Designation'])
    st.plotly_chart(fig)

if __name__=='__app__':
    run()

