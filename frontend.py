import streamlit as st
from fastcore.all import *
from fastai.text.all import Path, load_learner
import pathlib

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
#pathlib.PosixPath = temp


path = Path('model/mbti_text_classifier.pkl')
learn = load_learner(path)
# Dictionary with personality types and corresponding characters and images
di = {
    "ENFP": ["Satoru Gojo", "images/gojo_satoru.jpg"],
    "ISTP": ["Toji Fushiguro", "images/toji_fushiguro.jpg"],
    "ISFP": ["Yuji Itadori", "images/yuji_itadori.jpg"],
    "ENTJ": ["Ryomen Sukuna", "images/ryomen_sukuna.jpg"],
    "ISTJ": ["Megumi Fushiguro", "images/megumi_fushiguro.jpeg"],
    "ENFJ": ["Yuko Ozawa", "images/yuko_ozawa.png"],
    "ISFJ": ["Kasumi Miwa", "images/kasumi_miwa.jpeg"],
    "ESTP": ["Aoi Todo", "images/aoi_todo.jpeg"],
    "ESFP": ["Mai Zenin", "images/mai_zenin.jpeg"],
    "ESFJ": ["Akari Nitta", "images/akari_nitta.jpeg"],
    "ESTJ": ["Nobara Kugisaki", "images/nobara_kugisaki.jpg"],
    "INTJ": ["Kenjaku", "images/kenjaku.jpg"],
    "INFJ": ["Yuta Okkotsu", "images/yuta_okkotsu.jpg"],
    "INTP": ["Toge Inumaki", "images/toge_inumaki.jpg"],
    "ENTP": ["Mahito", "images/mahito.jpeg"],
    "INFP": ["Junpei Yoshino", "images/junpei_yoshino.jpeg"]
}


# Streamlit app layout
st.title("Which JJK Character are You?")
st.markdown("Enter a sentence to find out which JJK character matches your Myers-Briggs Personality Type!")

# Input text
sentence = st.text_input("")

# Check if input is provided
if sentence:
    
    # Get prediction from the model
    prediction = learn.predict(sentence)
    prediction = prediction[0]
    # Display the result
    character_name = di[prediction][0]
    character_image = di[prediction][1]
    
    st.write(f"## Your Myers-Briggs Personality Type is {prediction}")
    st.image(di[prediction][1], caption="Sunrise by the mountains",width=400)
    st.write(f"### You are most like {character_name}!")
