from nexora.ocr import NexoraOCR

ocr = NexoraOCR()

result = ocr.read("image.png")

print(result)