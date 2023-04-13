import time
from PIL import Image
from models.image_captioning.vit_gpt2.vit_gpt2_model import VITGPT2


model = VITGPT2(max_length=20, num_beams=5)
start = time.time()
image = Image.open("data/classmate.jpg")
print(model.describe(image))
print(time.time() - start)
