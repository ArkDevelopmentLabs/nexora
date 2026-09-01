from dataclasses import dataclass


@dataclass
class OCRResult:
    text: str
    confidence: float | None = None

    def __str__(self) -> str:
        return self.text