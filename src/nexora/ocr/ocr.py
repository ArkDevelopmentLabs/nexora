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
        """Initialize the NexoraOCR engine.

        Args:
            model: The model name to use. Must be one of the available models in MODEL_REGISTRY.
            device: Device placement for the model. Default is "auto".

        Raises:
            ValueError: If the specified model is not in MODEL_REGISTRY.
        """
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
        """Return a list of available OCR model names.

        Returns:
            A list of model names that can be used with NexoraOCR.
        """
        return list(MODEL_REGISTRY.keys())

    def read(self, image) -> OCRResult:
        """Extract text from an image using OCR.

        Args:
            image: An image to perform OCR on. Can be a PIL Image or a file path.

        Returns:
            An OCRResult containing the extracted text.
        """
        image = self.processor.load(image)

        text = self.model.predict(image)

        return OCRResult(
            text=text,
        )