# Text to 3D Model Generator

A Python-based application that converts textual descriptions into 3D models using Point-E, an open-source point cloud diffusion model developed by OpenAI.

---

## Features

- Text-to-3D conversion using advanced AI models
- Point cloud generation from textual descriptions
- OBJ file format output
- GPU acceleration support (when available)
- Simple command-line interface

---

## Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (optional, for faster processing)
- Windows 10/11 operating system

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/text-to-3d.git
cd text-to-3d
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Activate the virtual environment (if not already activated):

```bash
venv\Scripts\activate
```

2. Run the application:

```bash
python src/main.py
```

3. Enter your text prompt when asked. For example:

```
"A small toy car"
"A simple coffee cup"
"A basic chair"
```

The generated 3D model will be saved in the `output/` directory as an OBJ file.

---

## Project Structure

```
text-to-3d/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── text_to_3d.py
│   └── visualization.py
└── output/
```

---

## Technical Details

### Model Architecture

- Uses Point-E's `base40M` model for point cloud generation
- Implements text-to-embedding conversion using `base40M-textvec` model
- Converts point clouds to mesh representation

### Processing Pipeline

1. Text input processing
2. Text embedding generation
3. Point cloud creation
4. Mesh conversion
5. OBJ file export

---

## Limitations

- Generated models are basic representations
- Processing time depends on hardware capabilities
- GPU memory requirements may vary
- Output quality depends on input description clarity

---

## Troubleshooting

### Common Issues

**CUDA Out of Memory**  
*Solution:* Reduce batch size or use CPU mode

**Model Download Issues**  
*Solution:* Check internet connection and disk space

**Import Errors**  
*Solution:* Verify all dependencies are installed and Python version is compatible

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [OpenAI](https://openai.com) for the Point-E model
- PyTorch community
- Open-source 3D modeling tools

---

## Future Improvements

- Support for additional 3D file formats
- Enhanced mesh generation algorithms
- Web interface implementation
- Batch processing support
- More detailed geometry generation
