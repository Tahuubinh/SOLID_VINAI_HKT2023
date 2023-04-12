import streamlit as st
import streamlit.components.v1 as components

import os
import eyed3
from PIL import Image


# MUSIC_DIR = "./music"

# spotify links (somehow we got this :>)
RCM_NUMBER = 3 # number of recommendation
RCM_LINKS = ["https://open.spotify.com/embed/track/3a2Oftcs10wtzw6AmxuTMU?utm_source=generator", "https://open.spotify.com/embed/track/5d13XA4256WXujmAaFTr7O?utm_source=generator", "https://open.spotify.com/embed/track/3Dce2XbAZlQAFg2NWM2bb0?utm_source=generator"]

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
        for rcm_music in RCM_LINKS:
            # embedd the spotify music url
            components.iframe(rcm_music, height=80)
            buttons.append(st.button("Choose"))
        # st.write("[1. Don't let me down - Chainsmoker](https://www.youtube.com/watch?v=Io0fBr1XBUA)")
        # st.write("[2. The Chainsmokers - Closer (Lyric) ft. Halsey](https://www.youtube.com/watch?v=PT2_F-1esPk)")
    with st.expander("AI Generation", expanded=True):
        st.write("Audio1")
