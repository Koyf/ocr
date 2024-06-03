from enum import Enum

import pandas as pd
from easyocr import easyocr


class DataHeaders(int, Enum):
    bboard = 1
    text = 2
    conf = 3


def mapper(data_frame: pd.DataFrame) -> tuple[str, float]:
    text = data_frame.get("text").str.cat(sep=" ")
    accumulated_confident = data_frame.get("conf").mean()
    return text, accumulated_confident * 100


def read_text_from_image(image_path: str, language: str = "en") -> tuple[str, float]:
    reader = easyocr.Reader(lang_list=[language])
    text = reader.readtext(image=image_path)
    mapped_data = mapper(pd.DataFrame(text, columns=["bboard", "text", "conf"]))
    return mapped_data
