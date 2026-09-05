# Nexora

<p align="center">
  <img src="https://img.shields.io/badge/status-experimental-orange" alt="Status: Experimental"/>
  <img src="https://img.shields.io/badge/task-OCR%20%2F%20Text%20Extraction-red" alt="Task: OCR / Text Extraction"/>
  <img src="https://img.shields.io/badge/version-v0.1-blue" alt="Version: v0.1"/>
</p>

Nexora is a lightweight Python toolkit for working with AI models and machine learning capabilities.

The project is designed as a modular AI ecosystem, providing a unified Python interface for different model families and capabilities.

## Installation

Install Nexora from PyPI:

```bash
pip install nexora-ai
```

## Quick Start

### Optical Character Recognition

The OCR module provides a simple interface for extracting text from images.

```python
from nexora.ocr import NexoraOCR

ocr = NexoraOCR()

result = ocr.read("image.png")

print(result)
```

Nexora automatically loads the selected OCR model when inference is requested.

## Selecting an OCR Model

Nexora supports multiple OCR models through the `model` parameter.

### Default Model

If no model is specified, Nexora uses the 0.8B model:

```python
from nexora.ocr import NexoraOCR

ocr = NexoraOCR()

result = ocr.read("image.png")

print(result.text)
```

### 2B Model

To use the 2B model:

```python
from nexora.ocr import NexoraOCR

ocr = NexoraOCR(model="nexora-ocr-v0.1-2b")

result = ocr.read("image.png")

print(result.text)
```

### Available Models

You can retrieve the currently supported OCR models without loading a model:

```python
from nexora.ocr import NexoraOCR

models = NexoraOCR.available_models()

print(models)
```

Available models currently include:

```text
nexora-ocr-v0.1-0.8b
nexora-ocr-v0.1-2b
```

The model names are resolved internally to their corresponding model repositories.

## OCR

The OCR module provides an interface for extracting text from images using Nexora OCR models.

```python
from nexora.ocr import NexoraOCR

ocr = NexoraOCR(model="nexora-ocr-v0.1-2b")

result = ocr.read("image.png")

print(result.text)
```

The API is designed to keep OCR inference simple while allowing the underlying models and implementation to evolve independently.

### Device Selection

Nexora supports automatic device selection as well as explicit device configuration.

```python
from nexora.ocr import NexoraOCR

ocr = NexoraOCR(
    model="nexora-ocr-v0.1-2b",
    device="auto",
)

result = ocr.read("image.png")

print(result.text)
```

The default device configuration is `auto`.

## Models

The currently supported OCR models are:

| Model                  | Hugging Face Repository             | Size |
| ---------------------- | ----------------------------------- | ---: |
| `nexora-ocr-v0.1-0.8b` | `ArkAiLab-Adl/nexora-ocr-v0.1-0.8b` | 0.8B |
| `nexora-ocr-v0.1-2b`   | `ArkAiLab-Adl/nexora-ocr-v0.1-2b`   |   2B |

The models are distributed separately from the Python package through the Hugging Face Hub.

Nexora handles model loading and inference through its internal model interface, keeping model weights separate from the Python distribution.

## Project Structure

Nexora uses a modular architecture so different AI capabilities can be integrated through dedicated modules.

```text
nexora/

├── src/
│   └── nexora/
│       ├── __init__.py
│       │
│       └── ocr/
│           ├── __init__.py
│           ├── ocr.py
│           ├── model.py
│           ├── processor.py
│           └── result.py
│
├── tests/
├── README.md
├── LICENSE
├── requirements.txt
└── pyproject.toml
```

## Requirements

Nexora currently relies on the following core libraries:

- PyTorch
- Transformers
- Hugging Face Hub
- Accelerate
- SafeTensors
- Pillow
- NumPy

Python 3.10 or newer is required.

## Development

Clone the repository:

```bash
git clone https://github.com/ArkDevelopmentLabs/nexora

cd nexora
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the development dependencies:

```bash
pip install -r requirements.txt
```

Install Nexora in editable mode:

```bash
pip install -e .
```

## Roadmap

Nexora is being developed as a broader AI toolkit.

Planned improvements include:

- Improved OCR inference
- Batch inference
- GPU and CPU optimization
- Additional model integrations
- Model management utilities
- Additional computer vision capabilities
- Additional machine learning capabilities
- Improved inference and deployment utilities

The API and implementation details may evolve as the project develops.

## License

Nexora is licensed under the Apache License 2.0.

See the `LICENSE` file for the complete license text.

## Project

Nexora is developed by ArkDevLabs.

GitHub:

https://github.com/ArkDevelopmentLabs/nexora

PyPI:

https://pypi.org/project/nexora-ai/

## Status

Nexora is currently in alpha development.

The `0.1.x` releases are intended for experimentation, development, and early testing. APIs and implementation details may change between releases.
