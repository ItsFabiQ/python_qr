# QR Code Generator

This Python script generates a QR code from a user-provided link and saves it as an image file.

## Features

- Generates a QR code from a given link.
- Saves the QR code as an image file (`qr.png`).

## Prerequisites

- Python 3.6 or higher
- `qrcode` library
- `Pillow` library (for image processing)

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:
   ```bash
   pip install qrcode[pil]
   ```

## Usage

1. Run the script:
   ```bash
   python qr.py
   ```
2. Enter the link when prompted.
3. The script will generate a QR code and save it as `qr.png` in the current directory.

## Code Explanation

### Main Script

```python
import qrcode
from qrcode import *

qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(input("Put link here"), optimize=0)
qr.make(fit=False)

img = qr.make_image(fill='black', back_color='white')

img.save('qr.png')
```

### Explanation

- **Imports**: The script imports the `qrcode` library.
- **QRCode Object**: Creates a `QRCode` object with specified parameters:
  - `version`: Controls the size of the QR code.
  - `error_correction`: The error correction level.
  - `box_size`: The size of each box in the QR code.
  - `border`: The thickness of the border.
- **Adding Data**: Prompts the user to input a link and adds it to the QR code.
- **Generating the QR Code**: Generates the QR code with the specified parameters.
- **Saving the Image**: Saves the generated QR code as an image file (`qr.png`).

## License

This project is licensed under the MIT License.
