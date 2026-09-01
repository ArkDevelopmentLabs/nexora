from PIL import Image


class OCRProcessor:

    def load(self, image) -> Image.Image:
        if isinstance(image, Image.Image):
            return image.convert("RGB")

        return Image.open(image).convert("RGB")