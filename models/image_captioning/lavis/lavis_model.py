import torch
from PIL import Image

from lavis.models import load_model_and_preprocess


class BlipCaptionLargeCocoModel:
    def __init__(self, num_captions) -> None:
        self.num_captions = num_captions
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        # we associate a model with its preprocessors to make it easier for inference.
        self.model, self.vis_processors, _ = load_model_and_preprocess(
            name="blip_caption", model_type="large_coco", is_eval=True, device=self.device
        )

    def describe(self, raw_image):
        self.vis_processors.keys()
        image = self.vis_processors["eval"](
            raw_image).unsqueeze(0).to(self.device)
        # due to the non-determinstic nature of necleus sampling, you may get different captions.
        return self.model.generate({"image": image},
                                   use_nucleus_sampling=True, num_captions=self.num_captions)