from argparse import ArgumentParser
import logging
from pathlib import Path
import psutil

import cv2


LOGS_OUTPUT = 'data.log'
LOGS_FORMAT = '%(asctime)s\t%(levelname)s\t%(message)s'
LOGS_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'

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


main_logger = logging.getLogger(__name__)


def log_system_usage():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    main_logger.info(f'{cpu_usage = }%, {memory_usage = }%')


def read_image(file_name):
    logger = main_logger.getChild('read_image')
    logger.info('Starting to read the image.')

    file_path = ROOT_FOLDER / '0_static' / file_name
    file_path_string = str(file_path.absolute())
    result = cv2.imread(file_path_string, cv2.IMREAD_COLOR)

    try:
        assert result is not None, "No file data!"
        logger.info(f'File {file_name} loaded successfully. {result.shape = }')
    except AssertionError:
        logger.error(f'We have no data for {file_name=}')

    return result


def make_border(image):
    logger = main_logger.getChild('make_border')
    logger.info('Starting to make the image border.')

    result = cv2.copyMakeBorder(
        image,
        SMALL_BORDER,
        BIG_BORDER,
        SMALL_BORDER,
        SMALL_BORDER,
        cv2.BORDER_CONSTANT,
        value=BORDER_COLOR
    )

    logger.info('Image border has been made.')

    return result


def put_text(image, text):
    logger = main_logger.getChild('put_text')
    logger.info('Starting to put text onto image.')

    paste_location = (SMALL_BORDER, image.shape[0] - SMALL_BORDER)
    result = cv2.putText(
        image,
        text,
        paste_location,
        FONT,
        FONT_SCALE,
        FONT_COLOR,
        FONT_THICKNESS,
        cv2.LINE_AA
    )

    logger.info('Border has been put.')

    return result


def save_image(image):
    logger = main_logger.getChild('save_image')
    logger.info('Saving the image...')
    cv2.imwrite(RESULT_PATH, image)
    logger.info('Image saved.')


def parse_arguments():
    logger = main_logger.getChild('parse_arguments')
    parser = ArgumentParser(
        prog='Cat meme maker',
        description='Give me some cat, some text and enjoy the meme.',
    )
    parser.add_argument('-s', '--source', default=DEFAULT_CAT_FILE_NAME)
    parser.add_argument('-t', '--text', default=DEFAULT_CAT_TEXT)

    try:
        arguments = parser.parse_args()
    except SystemExit:
        logger.info('User tryed --help, terminating.\n')
        exit(0)

    for single_argument in vars(arguments):
        logger.info(f'"{single_argument}" has value "{getattr(arguments, single_argument)}"')

    return arguments


def main():
    main_logger.info('Execution started.')
    log_system_usage()

    arguments = parse_arguments()
    source_image = read_image(arguments.source)

    if source_image is None:
        main_logger.info('Image is empty. Terminating execution.\n')
        return

    bordered_image = make_border(source_image)
    result_image = put_text(bordered_image, arguments.text)
    save_image(result_image)

    log_system_usage()
    main_logger.info('Execution finished normally.\n')


if __name__ == '__main__':
    logging.basicConfig(
        format=LOGS_FORMAT,
        filename=LOGS_OUTPUT,
        level=logging.INFO,
        datefmt=LOGS_DATE_FORMAT,
    )
    main()
