import streamlit as st
import streamlit.components.v1 as components
from caption_generator import CaptionGenerator
from models.riffusion.text_to_music import generate_prompt, predict
from PIL import Image
from ChatGPT import *

GEN_MUSIC_OUT_DIR = "./model/riffusion"

def get_links(caption: str, genres: list, moods: list) -> list:
    print(caption)
    print(genres)
    print(moods)
    config = getGPTReady()
    chatbot = Chatbot(config=config)
    song_links = chatbot.recommendSong(
        n_songs=3, caption=caption, moods=moods, genres=genres)
    return [song['spotify_link'] for song in song_links]


def reload_images():
    image = Image.open(st.session_state.img)
    st.session_state.image = image.convert('RGB')
    # resize
    st.session_state.image.resize((256, 256))
    with img_col:
        st.image(st.session_state.image, use_column_width=True)


def reload_links():
    if 'img' in st.session_state and st.session_state.caption is not None:
        st.session_state.RCM_LINKS = get_links(
            st.session_state.caption, st.session_state.genres, st.session_state.moods)
    reload_images()


def reload_captions():
    reload_images()
    with img_col:
        if st.session_state.image is not None:
            cap_gen = CaptionGenerator(st.session_state.image)
            st.session_state.captions_ = cap_gen.generate(num=2, model='lavis')


# def set_selected_song():
#     st.session_state.type_ = 'gen'
#     st.session_state.id_ = 0
#     reload_images()

def reload_gen_music():
    if 'img' in st.session_state and st.session_state.caption is not None:
        prompt, negative_prompt = generate_prompt(
            st.session_state.caption, st.session_state.genres, st.session_state.moods)
        out, _ = predict(prompt, negative_prompt)
        with gen_expander:
            audio_file = open(os.path.join(".", "models", "riffusion", "output.wav"), 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes)
            # button = st.button("Choose", key=f"gen", on_click=set_selected_song)
    reload_images()

if 'RCM_NUMBER' not in st.session_state:
    st.session_state.RCM_NUMBER = 1
if 'RCM_LINKS' not in st.session_state:
    st.session_state.RCM_LINKS = []
if 'id_' not in st.session_state:
    st.session_state.id_ = -1
if 'type_' not in st.session_state:
    st.session_state.type_ = None
if 'captions_' not in st.session_state:
    st.session_state.captions_ = []


st.title("MUSIC GENERATION APP")
st.header("Made by team SOLID")

img_col, music_col = st.columns(2, gap="large")
gen_expander = None
with img_col:
    st.file_uploader("Please upload an image file", type=[
                     "jpg", "png", "tif"], on_change=reload_captions, key="img")
    image_placeholder = st.empty()
    if st.session_state.img is None:
        st.text("Please upload an image file")

    # generate captions and display them
    st.radio("Generated captions", st.session_state.captions_,
             key='caption',
             on_change=reload_images
             )
    caption = None
    if caption is not None:
        st.write(f"Caption: {caption}")
    st.multiselect(
        'Genre :musical_note:',
        ['Pop', 'Rock', 'Ballad', 'EDM', 'R&B', 'Soul', 'Rap'],
        on_change=reload_images,
        key='genres'
    )

    st.multiselect(
        'Mood :kissing:',
        ['Happy', 'Exciting', 'Sad', 'Nervous', 'Neutral'],
        on_change=reload_images,
        key='moods'
    )

with music_col:
    with st.expander("Recommendation", expanded=True):
        # buttons = []
        # get recommendation links and display them
        for i, rcm_music in enumerate(st.session_state.RCM_LINKS):
            # embedd the spotify music url
            components.iframe(rcm_music, height=80)
            # buttons.append(st.button("Choose", key=f"rcm_{i}"))
        # for i, button in enumerate(buttons):
        #     if button:
        #         st.session_state.type_ = 'rcm'
        #         st.session_state.id_ = i
        reload_ = st.button("Reload", key="reload_rcm", on_click=reload_links)

    gen_expander = st.expander("AI Generation", expanded=True)
    with gen_expander:
        # generate music and display them
        st.write(f"Audio 1")

        reload_gen = st.button("Reload", key="reload_gen", on_click=reload_gen_music)
# st.write(
#     f"You choose song of type {st.session_state.type_} with id {st.session_state.id_+1}")
