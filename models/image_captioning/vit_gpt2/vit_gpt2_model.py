from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image


class VITGPT2:
    def __init__(self, max_length, num_beams) -> None:
        self.model = VisionEncoderDecoderModel.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning")
        self.feature_extractor = ViTImageProcessor.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning")

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.max_length = 20
        self.num_beams = 5
        self.gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

    def describe(self, i_image):
        pixel_values = self.feature_extractor(
            images=[i_image], return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(self.device)

        output_ids = self.model.generate(pixel_values, **self.gen_kwargs)

        pred = self.tokenizer.batch_decode(
            output_ids, skip_special_tokens=True)
        return pred
