from readers.tesseract import read_text_from_image as tesseract_reader
from readers.easyocr_reader import read_text_from_image as easyocr_reader
from utils import calculate_predicted_accuracy, parse_args
from validators.gpt2 import validate_text
from constants import EASYOCR_CHARACTER


def main(image_path: str, output_path: str, model: str, validate: bool = False):
    if model == EASYOCR_CHARACTER:
        text, confident = easyocr_reader(image_path)
    else:
        text, confident = tesseract_reader(image_path)

    with open(output_path, "w") as f:
        f.write(text)

    print(f"Confident: {confident:.2f}%")

    if validate:
        perplexity = validate_text(text)
        predicted_accuracy = calculate_predicted_accuracy(perplexity)
        print(f"Predicted accuracy: {predicted_accuracy:.2f}%")


if __name__ == "__main__":
    main(**parse_args())
