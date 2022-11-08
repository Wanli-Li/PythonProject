import streamlit as st

from PIL import Image
image = Image.open('PictureDemo/1.jpg')

st.image(image, caption='Sunrise by the mountains')