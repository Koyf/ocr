# OCR Email extracter

## Install dependencies

1. Install Python packages:

    ```sh
    pip install -r requirements.txt
    ```

2. Install Tesseract:

    ### For Ubuntu:

    ```sh
    sudo apt-get update
    sudo apt-get install tesseract-ocr
    sudo apt-get install libtesseract-dev
    ```

    ### For macOS:

    ```sh
    brew install tesseract
    ```

    ### For Windows:
    ## 🫡
    

## Usage

Run script:

```sh
python src/main.py [-h] [-m {t,e}] [-v] image output
```

```
positional arguments:
  image                 image path
  output                output path

options:
  -h, --help            show this help message and exit
  -m {t,e}, --model {t,e}
                        Choose model to recognize text: 't' - Tesseract (default); 'e' - EasyOCR
  -v, --validate        Validate recognized text by language model (GPT-2)
```