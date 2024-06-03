from enum import Enum

import pytesseract
import pandas as pd


class DataHeaders(int, Enum):
    level = 1
    page_num = 2
    block_num = 3
    par_num = 4
    line_num = 5
    word_num = 6
    left = 7
    top = 8
    width = 9
    height = 10
    conf = 11
    text = 12


def mapper(data_frame: pd.DataFrame) -> tuple[str, float]:
    text = data_frame.get("text").str.cat(sep=" ")
    accumulated_confident = data_frame.get("conf").mean()
    return text, accumulated_confident


def read_text_from_image(image_path: str, language: str = "eng") -> tuple[str, float]:
    data = pytesseract.image_to_data(
        image_path, lang=language, output_type=pytesseract.Output.DATAFRAME
    )
    mapped_data = mapper(data)
    return mapped_data
