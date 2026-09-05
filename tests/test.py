from nexora.ocr import NexoraOCR

ocr = NexoraOCR(model="nexora-ocr-v0.1-2b")

result = ocr.read("image.png")

print(result)