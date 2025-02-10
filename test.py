import streamlit as st
import os 
import pandas as pd
bg_image_url = "https://c4.wallpaperflare.com/wallpaper/670/883/685/plexus-atoms-neutrons-electrons-wallpaper-preview.jpg"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{bg_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        opacity: 0,4;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("DBMS ")
st.write ("Database Managesdadmentdsad System as a crucial thing for a beginner to learn back-end ")
a = 7 
st.button("im button")
st.subheader("This is Ex Dataframe")
pf = pd.DataFrame({
    'Name' : ['Bihan','alzam','bihan'],
    'Hobby' : ['soccer','chess','video game']
})
st.data_editor(pf)
