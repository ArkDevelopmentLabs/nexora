# Nexora

<p align="center">
  <img src="https://img.shields.io/badge/status-experimental-orange" alt="Status: Experimental"/>
  <img src="https://img.shields.io/badge/base_model-Qwen3.5%200.8B-blueviolet" alt="Base Model: Qwen3.5 0.8B"/>
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

```python
from nexora.ocr import NexoraOCR

ocr = NexoraOCR()

result = ocr.read("image.png")

print(result)
```

Nexora automatically loads the configured model and performs inference using the provided image.

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

## OCR

The OCR module provides an interface for extracting text from images using Nexora OCR models.

```python
from nexora.ocr import NexoraOCR

ocr = NexoraOCR()

result = ocr.read("image.png")

print(result.text)
```

The API is designed to keep OCR inference simple while allowing the underlying model and implementation to evolve independently.

## Model

The initial OCR implementation uses:

```text
ArkAiLab-Adl/nexora-ocr-v0.1-0.8b
```

The model is based on the Qwen3.5-0.8B architecture and is distributed through the Hugging Face Hub.

Nexora keeps model weights separate from the Python distribution and handles model loading and inference through its internal model interface.

## Requirements

Nexora currently relies on the following core libraries:

- PyTorch
- Transformers
- Hugging Face Hub
- Accelerate
- SafeTensors
- Pillow
- NumPy

Python 3.10 or newer is recommended.

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
