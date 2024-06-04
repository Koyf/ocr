import argparse
import re


from constants import EMPIRICAL_PERPLEXITY, EASYOCR_CHARACTER, TESSERACT_CHARACTER


def calculate_predicted_accuracy(perplexity: float):
    coefficient = 1 - perplexity / EMPIRICAL_PERPLEXITY
    accuracy = max(coefficient, 0)
    return accuracy * 100


def extract_emails(text: str) -> list[str]:
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_list = re.findall(email_pattern, text)
    return email_list


def format_emails(email_list: list[str]) -> str:
    return "\n".join(email_list)


def parse_args():
    parser = argparse.ArgumentParser(description="OCR")
    parser.add_argument("image", type=str, help="image path")
    parser.add_argument("output", type=str, help="output path")
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        choices=[TESSERACT_CHARACTER, EASYOCR_CHARACTER],
        default=TESSERACT_CHARACTER,
        help="Choose model to recognize text: 't' - Tesseract (default); 'e' - EasyOCR",
    )
    parser.add_argument(
        "-v",
        "--validate",
        action="store_true",
        help="Validate recognized text by language model (GPT-2)",
    )

    args = parser.parse_args()

    return {
        "image_path": args.image,
        "output_path": args.output,
        "model": args.model,
        "validate": args.validate,
    }
