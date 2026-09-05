from .model import NexoraModel
from .processor import OCRProcessor
from .result import OCRResult


MODEL_REGISTRY = {
    "nexora-ocr-v0.1-0.8b": "ArkAiLab-Adl/nexora-ocr-v0.1-0.8b",
    "nexora-ocr-v0.1-2b": "ArkAiLab-Adl/nexora-ocr-v0.1-2b",
}


class NexoraOCR:
    def __init__(
        self,
        model: str = "nexora-ocr-v0.1-0.8b",
        device: str = "auto",
    ):
        if model not in MODEL_REGISTRY:
            available_models = ", ".join(MODEL_REGISTRY.keys())

            raise ValueError(
                f"Unknown OCR model: '{model}'. "
                f"Available models: {available_models}"
            )

        self.processor = OCRProcessor()

        model_id = MODEL_REGISTRY[model]

        self.model = NexoraModel(
            model_name=model_id,
            device=device,
        )

        self.model_name = model
        self.model_id = model_id

    @classmethod
    def available_models(cls):
        return list(MODEL_REGISTRY.keys())

    def read(self, image) -> OCRResult:
        image = self.processor.load(image)

        text = self.model.predict(image)

        return OCRResult(
            text=text,
        )