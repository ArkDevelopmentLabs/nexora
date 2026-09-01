import torch
from transformers import AutoProcessor, AutoModelForMultimodalLM


class NexoraModel:
    def __init__(
        self,
        model_name: str = "ArkAiLab-Adl/nexora-ocr-v0.1-0.8b",
        device: str = "auto",
    ):
        self.model_name = model_name
        self.device = device

        self.processor = None
        self.model = None

    def load(self):
        """Load the Nexora OCR model and processor."""

        self.processor = AutoProcessor.from_pretrained(
            self.model_name
        )

        self.model = AutoModelForMultimodalLM.from_pretrained(
            self.model_name,
            device_map=self.device,
            torch_dtype="auto",
        )

        self.model.eval()

    def predict(
        self,
        image,
        prompt: str = "Transcribe the text in this image exactly as it appears.",
        max_new_tokens: int = 256,
    ) -> str:
        """Run OCR inference on an image."""

        if self.model is None:
            self.load()

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": image,
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    },
                ],
            }
        ]

        inputs = self.processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        )

        inputs = inputs.to(self.model.device)

        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
            )

        input_length = inputs["input_ids"].shape[-1]

        generated_tokens = outputs[
            0,
            input_length:
        ]

        text = self.processor.decode(
            generated_tokens,
            skip_special_tokens=True,
        )

        return text.strip()