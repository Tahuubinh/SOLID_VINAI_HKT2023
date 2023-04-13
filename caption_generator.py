from models.image_captioning.vit_gpt2.vit_gpt2_model import VITGPT2
# from models.image_captioning.lavis.lavis_model import BlipCaptionLargeCocoModel


class CaptionGenerator:
    def __init__(self, image):
        self.image = image

    def generate(self, num=3, model='vitgpt2'):
        assert model in ['vitgpt2', 'lavis'], "Model is not supported!"
        if model == 'vitgpt2':
            gen_model = VITGPT2(max_length=20, num_beams=1)
        # if model == "lavis":
        #     model = BlipCaptionLargeCocoModel(num_captions=num)
        return gen_model.describe(self.image)
