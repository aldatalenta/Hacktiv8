import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from os import access
from io import BytesIO
import requests
from tensorflow.keras.models import load_model


st.set_page_config(
    page_title='Predict',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load Model
best_model = load_model('model.h5')
best_model

def run ():
    # Variable for image
    img = None

    # Prediction
    def img_predict(img):
        pred = np.array(img)[:, :, :3]
        pred = tf.image.resize(pred, size=(180, 180))
        pred = pred / 255.0

        res = int(tf.round(best_model.predict(x=tf.expand_dims(pred, axis=0))))
        res = "Biodegradable Material" if res == 0 else "Non-biodegradable Material"
        title = f"<h2 style='text-align:center'>{res}</h2>"
        st.markdown(title, unsafe_allow_html=True)
        st.image(img, use_column_width=True)

    # Title
    st.title("Image Classification for Non and Biodegradable Material")
    st.subheader('This app classifies waste material from given image')

    # Image Upload Option
    choose = st.selectbox("Select Input Method", ["Upload an Image", "URL from Web"])

    if choose == "Upload an Image":  # If user chooses to upload image
        file = st.file_uploader("Upload an image...", type=["jpg", "png", 'Tiff'])
        if file is not None:
            img = Image.open(file)
    else:  # If user chooses to upload image from url
        url = st.text_area("URL", placeholder="Put URL here")
        if url:
            try:  # Try to get the image from the url
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
            except:  # If the url is not valid, show error message
                st.error(
                    "Failed to load the image. Please use a different URL or upload an image."
                )

    if img is not None:
        predict = st.button("Predict")
        if predict:
            img_predict(img)

if __name__=='__app__':
    run()
