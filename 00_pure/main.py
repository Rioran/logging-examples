from argparse import ArgumentParser
from pathlib import Path

import cv2


CURRENT_FOLDER = Path(__file__).parent
ROOT_FOLDER = CURRENT_FOLDER.parent
DEFAULT_CAT_FILE_NAME = 'cat.jpg'
CAT_PATH = str((ROOT_FOLDER / '0_static' / DEFAULT_CAT_FILE_NAME).absolute())
RESULT_PATH = str((CURRENT_FOLDER / 'result.jpg').absolute())

DEFAULT_CAT_TEXT = 'Kneel, human!'

FONT = cv2.FONT_HERSHEY_PLAIN
FONT_SCALE = 7
FONT_COLOR = (255, 255, 255)  # BGR, not RGB!!!
FONT_THICKNESS = 7
FONT_LINE = cv2.LINE_AA

BORDER_COLOR = (0, 0, 0)
SMALL_BORDER = 20
BIG_BORDER = 120


def read_image(file_name):
    file_path = ROOT_FOLDER / '0_static' / file_name
    file_path_string = str(file_path.absolute())
    return cv2.imread(file_path_string, cv2.IMREAD_COLOR)


def make_border(image):
    return cv2.copyMakeBorder(
        image,
        SMALL_BORDER,
        BIG_BORDER,
        SMALL_BORDER,
        SMALL_BORDER,
        cv2.BORDER_CONSTANT,
        value=BORDER_COLOR
    )


def put_text(image, text):
    paste_location = (SMALL_BORDER, image.shape[0] - SMALL_BORDER)
    return cv2.putText(
        image,
        text,
        paste_location,
        FONT,
        FONT_SCALE,
        FONT_COLOR,
        FONT_THICKNESS,
        cv2.LINE_AA
    )


def save_image(image):
    cv2.imwrite(RESULT_PATH, image)


def parse_arguments():
    parser = ArgumentParser(
        prog='Cat meme maker',
        description='Give me some cat, some text and enjoy the meme.'
    )
    parser.add_argument('-s', '--source', default=DEFAULT_CAT_FILE_NAME)
    parser.add_argument('-t', '--text', default=DEFAULT_CAT_TEXT)
    arguments = parser.parse_args()
    return arguments


def main():
    arguments = parse_arguments()
    source_image = read_image(arguments.source)
    bordered_image = make_border(source_image)
    result_image = put_text(bordered_image, arguments.text)
    save_image(result_image)


if __name__ == '__main__':
    main()
