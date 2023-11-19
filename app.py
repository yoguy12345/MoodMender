import cv2
import streamlit as st
import numpy as np
from openai import OpenAI
import os
import requests

from camera_input_live import camera_input_live

OPENAI_API_KEY = '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'

def main():
    # st.title("Webcam Video Capture with Streamlit")

    # # OpenCV video capture
    # cap = cv2.VideoCapture(0)

    # if not cap.isOpened():
    #     st.error("Error: Unable to open webcam.")
    #     return

    # # Set video width and height
    # cap.set(3, 640)
    # cap.set(4, 480)

    # image_container = st.empty()
    # # Streamlit loop
    # while True:
    #     ret, frame = cap.read()

    #     if not ret:
    #         st.error("Error: Unable to read frame.")
    #         break

    #     # Display the frame in Streamlit
    #     image_container.empty()
    #     st.image(frame, channels="BGR", use_column_width=True)

    # # Release the webcam when the app is closed
    # cap.release()

    # image = camera_input_live()

    # st.image(image)
    
    st.title("OpenAI API Test")

    # st.write("You:")
    user_msg = st.text_input('You: ')
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a trained psychotherapist, specializing in providing stress management strategies for people with ADHD. Give short responses for every query, less than 4 sentences. "},
            {"role": "user", "content": user_msg}
        ]
    )
    
    # "My stress levels are at 80%. I cant sit still. What do I do to focus on my work?"
    
    st.write(completion.choices[0].message.content)
    
        
# if __name__== "main":
main()
