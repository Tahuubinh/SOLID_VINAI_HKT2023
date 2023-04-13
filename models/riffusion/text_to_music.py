from diffusers import DiffusionPipeline
from riffusion.spectrogram_image_converter import SpectrogramImageConverter
from riffusion.spectrogram_params import SpectrogramParams
from io import BytesIO
from IPython.display import Audio
import torch

pipe = DiffusionPipeline.from_pretrained("riffusion/riffusion-model-v1")
if torch.cuda.is_available():
    pipe = pipe.to("cuda")
else:
    pipe = pipe.to("cpu")


params = SpectrogramParams()
converter = SpectrogramImageConverter(params)


def generate_prompt(caption: str, genres: list, moods: list):
    moods_str = ", ".join(moods)
    genres_str = ", ".join(genres)
    mood_prompt = f"{moods_str} vibe, " if len(moods) else ""
    genre_prompt = f"{genres_str} genre, " if len(genres) else ""
    prompt = f"A song with content related to {caption}. " + mood_prompt + genre_prompt
    negative_prompt = "bad quality, out of context, wrong vibe, wrong genre"
    return prompt, negative_prompt

def predict(prompt, negative_prompt):
    spec = pipe(
        prompt,
        negative_prompt=negative_prompt,
        width=768,
    ).images[0]

    wav = converter.audio_from_spectrogram_image(image=spec)
    wav.export('output.wav', format='wav')
    return 'output.wav', spec


# prompt = "solo piano piece, classical"  # @param {type:"string"}
# negative_prompt = "drums"  # @param {type:"string"}

# path, spec = predict(prompt, negative_prompt)

# display(spec)
# Audio('output.wav')
