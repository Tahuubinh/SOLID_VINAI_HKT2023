from diffusers import DiffusionPipeline
from riffusion.spectrogram_image_converter import SpectrogramImageConverter
from riffusion.spectrogram_params import SpectrogramParams
from io import BytesIO
from IPython.display import Audio

pipe = DiffusionPipeline.from_pretrained("riffusion/riffusion-model-v1")
pipe = pipe.to("cuda")


params = SpectrogramParams()
converter = SpectrogramImageConverter(params)

def predict(prompt, negative_prompt):
    spec = pipe(
        prompt,
        negative_prompt=negative_prompt,
        width=768,
    ).images[0]
    
    wav = converter.audio_from_spectrogram_image(image=spec)
    wav.export('output.wav', format='wav')
    return 'output.wav', spec

prompt = "solo piano piece, classical"#@param {type:"string"}
negative_prompt = "drums"#@param {type:"string"}

path, spec = predict(prompt, negative_prompt)

display(spec)
Audio('output.wav')