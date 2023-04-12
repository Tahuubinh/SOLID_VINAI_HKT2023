import streamlit as st
import streamlit.components.v1 as components

import os
from PIL import Image


# MUSIC_DIR = "./music"

# spotify links (somehow we got this :>)
RCM_NUMBER = 3 # number of recommendation
RCM_LINKS = ["https://open.spotify.com/embed/track/3a2Oftcs10wtzw6AmxuTMU?utm_source=generator", "https://open.spotify.com/embed/track/5d13XA4256WXujmAaFTr7O?utm_source=generator", "https://open.spotify.com/embed/track/3Dce2XbAZlQAFg2NWM2bb0?utm_source=generator"]

if 'id_' not in st.session_state:
    st.session_state.id_ = -1
if 'type_' not in st.session_state:
    st.session_state.type_ = None   
if 'captions_' not in st.session_state:
    st.session_state.captions_ = ["a cat sitting", "a sad cat"]   

st.title("MUSIC GENERATION APP")
st.header("Made by team SOLID")

img_col, music_col = st.columns(2, gap="large")

with img_col:
    file = st.file_uploader("Please upload an image file", type=["jpg", "png", "tif"])
    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        image = image.convert('RGB')
        # resize
        image.resize((256, 256))
        st.image(image, use_column_width=True)
    # generate captions and display them
    st.radio("Generated captions", st.session_state.captions_)
    caption = None
    if caption is not None:
        st.write(f"Caption: {caption}")
    genres = st.multiselect(
    'Genre :musical_note:',
    ['Pop', 'Rock', 'Ballad', 'EDM', 'R&B', 'Soul', 'Rap'],
    )

    moods = st.multiselect(
    'Mood :kissing:',
    ['Happy', 'Exciting', 'Sad', 'Nervous', 'Neutral'],
    )

with music_col:
    with st.expander("Recommendation", expanded=True):
        buttons = []
        # get recommendation links and display them
        for i, rcm_music in enumerate(RCM_LINKS):
            # embedd the spotify music url
            components.iframe(rcm_music, height=80)
            buttons.append(st.button("Choose", key=f"rcm_{i}"))
        for i, button in enumerate(buttons):
            if button:
                st.session_state.type_ = 'rcm'
                st.session_state.id_ = i

    with st.expander("AI Generation", expanded=True):
        # generate music and display them
        buttons = []
        for i in range(3):
            st.write(f"Audio{i}")
            buttons.append(st.button("Choose", key=f"gen_{i}"))
        for i, button in enumerate(buttons):
            if button:
                st.session_state.type_ = 'gen'
                st.session_state.id_ = i       

st.write(f"You choose song of type {st.session_state.type_} with id {st.session_state.id_}")
