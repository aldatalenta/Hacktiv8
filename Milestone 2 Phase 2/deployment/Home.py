import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Non and Biodegradable Material',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Non and Biodegradable Material Prediction')

    # Membuat Sub Header
    st.subheader('Background of Non and Biodegradable Material Dataset Analysis')

    # Menambahkan Gambar
    image = Image.open('waste.jpg')
    st.image(image, caption='Non and Biodegradable Material')

    # Menambahkan Deskripsi
    st.write('This page was created by **Alda Nesti Talenta Pakpahan**')
    st.write('# Description')

    # Magic Syntax
    st.write(
    '''
    As we all know that Waste/Garbage has become commonplace in many countries in the world. 
    The definition of waste itself is interpreted as a final product that can no longer be used by humans, or also known as residue.
    The problem lies in How do we manage this waste, while we can't use it anymore?. 
    On the other hand, there are several countries that have problems related to waste because the rate of waste production is not proportional to the efforts to manage it.
    These things can be a big problem for the ecosystem.
    '''
    '''
    With this dataset, it is hoped that I can help waste management efforts with Computer Vision technology.
    With this technology, we can identify, track, sort or classify which are included in biodegradable and non-biodegradable waste, and can process it as needed.
    '''
    '''
    Biodegradable, means that it contains materials that can be broken down naturally by microorganisms, such as food, plants, fruits, etc.
    Waste from this material can be processed into compost.
    While Non-biodegradable, means it contains materials that cannot be decomposed naturally, for example plastic, metal, inorganic elements, etc.
    The waste from this material will be recycled into new materials.
    ''')

    # Membuat Garis Lurus
    st.markdown('---')

    # Show DataFrame
    st.write('The dataset used is Non and Biodegradable Material Dataset')
    st.write('Please access the dataset on: [Kaggle](https://www.kaggle.com/datasets/rayhanzamzamy/non-and-biodegradable-waste-dataset)')

if __name__=='__app__':
    run()