from models.image_captioning.lavis.lavis_model import BlipCaptionLargeCocoModel


model = BlipCaptionLargeCocoModel(num_captions=3)
print(model.describe("models/image_captioning/lavis/docs/_static/merlion.png"))
