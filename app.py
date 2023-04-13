import streamlit as st
import streamlit.components.v1 as components
import random
from caption_generator import CaptionGenerator
import os
from PIL import Image


def get_links(captions: list, genres: list, moods: list) -> list:
    return random.choice([["https://open.spotify.com/embed/track/7wj9sGlHGTMQ28liyi48hz?utm_source=generator"], ["https://open.spotify.com/embed/track/3a2Oftcs10wtzw6AmxuTMU?utm_source=generator"], ["https://open.spotify.com/embed/track/5d13XA4256WXujmAaFTr7O?utm_source=generator"]])

def reload_links():
    if 'img' in st.session_state:
        st.session_state.RCM_LINKS = get_links(st.session_state.captions_, st.session_state.genres, st.session_state.moods)

def reload_captions():
    image = Image.open(st.session_state.img)
    st.session_state.image = image.convert('RGB')
    # resize
    st.session_state.image.resize((256, 256))
    with img_col:
        st.image(st.session_state.image, use_column_width=True)
        if st.session_state.image is not None:
            cap_gen = CaptionGenerator(st.session_state.image)
            st.session_state.captions_ = cap_gen.generate(num=2)
    # captions must not be None
    st.session_state.RCM_LINKS = get_links(st.session_state.captions_, st.session_state.genres, st.session_state.moods)
 

if 'RCM_NUMBER' not in st.session_state:
    st.session_state.RCM_NUMBER = 3
if 'RCM_LINKS' not in st.session_state:
    st.session_state.RCM_LINKS = []
if 'id_' not in st.session_state:
    st.session_state.id_ = -1
if 'type_' not in st.session_state:
    st.session_state.type_ = None   
if 'captions_' not in st.session_state:
    st.session_state.captions_ = []
# if 'genres' not in st.session_state:
#     st.session_state.genres = None
# if 'moods' not in st.session_state:
#     st.session_state.moods = None
# if 'image' not in st.session_state:
#     st.session_state.image = None
# if 'img_file' not in st.session_state:
#     st.session_state.img_file = None

st.title("MUSIC GENERATION APP")
st.header("Made by team SOLID")

img_col, music_col = st.columns(2, gap="large")
with img_col:
    st.file_uploader("Please upload an image file", type=["jpg", "png", "tif"], on_change=reload_captions, key="img")
    if st.session_state.img is None:
        st.text("Please upload an image file")

    # generate captions and display them    
    st.radio("Generated captions", st.session_state.captions_, on_change=reload_links)
    caption = None
    if caption is not None:
        st.write(f"Caption: {caption}")
    st.multiselect(
    'Genre :musical_note:',
    ['Pop', 'Rock', 'Ballad', 'EDM', 'R&B', 'Soul', 'Rap'],
    on_change=reload_links,
    key='genres'
    )

    st.multiselect(
    'Mood :kissing:',
    ['Happy', 'Exciting', 'Sad', 'Nervous', 'Neutral'],
    on_change=reload_links,
    key='moods'
    )

with music_col:
    with st.expander("Recommendation", expanded=True):
        buttons = []
        # get recommendation links and display them
        for i, rcm_music in enumerate(st.session_state.RCM_LINKS):
            # embedd the spotify music url
            components.iframe(rcm_music, height=80)
            buttons.append(st.button("Choose", key=f"rcm_{i}"))
        for i, button in enumerate(buttons):
            if button:
                st.session_state.type_ = 'rcm'
                st.session_state.id_ = i
        reload_ = st.button("Reload", on_click=reload_links)

    with st.expander("AI Generation", expanded=True):
        # generate music and display them
        buttons = []
        for i in range(st.session_state.RCM_NUMBER):
            st.write(f"Audio{i}")
            buttons.append(st.button("Choose", key=f"gen_{i}"))
        for i, button in enumerate(buttons):
            if button:
                st.session_state.type_ = 'gen'
                st.session_state.id_ = i       

st.write(f"You choose song of type {st.session_state.type_} with id {st.session_state.id_}")
