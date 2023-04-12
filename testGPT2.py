import time

from models.image_captioning.vit_gpt2.vit_gpt2_model import VITGPT2


model = VITGPT2(max_length=20, num_beams=5)
start = time.time()
print(model.describe('data/classmate.jpg'))
print(time.time() - start)
