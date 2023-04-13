import time

from models.image_captioning.lavis.lavis_model import BlipCaptionLargeCocoModel


model = BlipCaptionLargeCocoModel(num_captions=2)
start = time.time()
# print(model.describe("models/image_captioning/lavis/docs/_static/merlion.png"))
# print(model.describe("data/corgy_jump.png"))
print(model.describe("data/winning_girl.jpg"))
print(time.time() - start)
