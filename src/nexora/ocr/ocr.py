from .model import NexoraModel
from .processor import OCRProcessor
from .result import OCRResult


class NexoraOCR:
    def __init__(
        self,
        model: str = "ArkAiLab-Adl/nexora-ocr-v0.1-0.8b",
        device: str = "auto",
    ):
        self.processor = OCRProcessor()

        self.model = NexoraModel(
            model_name=model,
            device=device,
        )

    def read(self, image) -> OCRResult:
        image = self.processor.load(image)

        text = self.model.predict(image)

        return OCRResult(
            text=text,
        )