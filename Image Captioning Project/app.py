# A basic image captioning application using Gemini Pro API Vision

from dotenv import load_dotenv
load_dotenv() # Loading environment variables

import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY")) # Getting the API key from .env file at the time of configuration

# Function to load Gemini Pro model and get responses using vision api
# gemini-pro-vision - it checks all info on image and generate text
model = genai.GenerativeModel("gemini-pro-vision") 
def get_gemini_response(input, image): # input is what I really want to do with the image 
    if input != "":
        response = model.generate_content([input, image]) # eg input = blog on image and image = inserted image
    else:
        response = model.generate_content(image) # just analyse and describes the image iits own without any constraints
    return response.text

# Initialise the streamlit app

st.set_page_config(page_title = "Gemini Image Demo") 
st.header("Caption Generator using Gemini API")
input = st.text_input("Input (Suggested to write Generate Caption about image): ", key = "input") # text box for input

# taking image as input from user
uploaded_file = st.file_uploader("Choose any file :) ", type = ["jpg", "jpeg", "png"])
image = ""

# Logic for taking image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Image Uploaded.", use_column_width = True)

submit = st.button("Generate Caption about image")

# if button clicked
if submit:
    response = get_gemini_response(input, image)
    # displaying the response
    st.subheader("Generated Caption is")
    st.write(response)

footer = """
---

<p style="text-align:center;">Made by Sathwik with ❤️ | © 2023 All rights reserved.</p>
"""
# making the text to align to center
st.markdown(footer, unsafe_allow_html=True)