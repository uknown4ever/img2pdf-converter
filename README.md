# Image to PDF Converter

A simple Python script that converts images (JPG, JPEG, PNG) into a single PDF file.

## Features

- ✅ Converts multiple images to one PDF
- ✅ Supports JPG, JPEG, and PNG formats
- ✅ Automatically sorts images alphabetically
- ✅ Simple and easy to use
- ✅ No command-line arguments needed

## Prerequisites

- Python 3.6 or higher
- `img2pdf` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/uknown4ever/img2pdf-converter.git
cd img2pdf-converter
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Or  install directly:
```bash
pip install img2pdf
```

## Usage

1. Create a folder named `my_images` in the same directory as the script

2. Add your images to the `my_images` folder:
```
img2pdf-converter/
├── img2pdf_converter.py
└── my_images/
    ├── page1.jpg
    ├── page2.jpg
    └── page3.png
```

3. Run the script:
```bash
python img2pdf_converter.py
```

4. Find your `output.pdf` in the same directory!

## Example

```bash
# Create the images folder
mkdir my_images

# Add your images to my_images/

# Run the converter
python img2pdf_converter.py
```

Output:
```
Success! Created output.pdf from 3 image(s)
Images converted: page1.jpg, page2.jpg, page3.png
```

## Supported Image Formats

- `.jpg`
- `.jpeg`
- `.png`

## Error Handling

The script will notify you if:
- The `my_images` folder doesn't exist
- No image files are found in the folder
- There's an error during PDF creation

## Project Structure

```
img2pdf-converter/
├── img2pdf_converter.py    # Main script
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── my_images/              # Put your images here (you create this)
└── output.pdf              # Generated PDF (created by script)
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
