from PutText import PutText
from PIL import Image
import os
import cv2 as cv
import argparse
import random
from pathlib import Path
import csv



def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_data_root", type=str)

    return parser.parse_args()

def main():
    args = get_parser()
    base_data_root = args.base_data_root
    if not os.path.exists(base_data_root):
        raise NotImplementedError()
    if not os.path.exists("generate_images"):
        os.makedirs("generate_images")

    text_list = []
    with open('text/hiragana.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            text_list.append(row[0])

    # import pdb;pdb.set_trace()

    im_root_path = Path(base_data_root)
    for im_path in list(im_root_path.glob("*")):
        cv_image = cv.imread(im_path.as_posix())

        # import pdb;pdb.set_trace()

        font_root_path = Path("font")
        for fn, font_path in enumerate(list(font_root_path.glob("*"))):
            for i in range(10):
                point = tuple(random.choices(list(range(0, 200)), k=2))
                font_size = random.randrange(10, 200, 5)
                color = tuple(random.choices(list(range(0, 255)), k=3))
                text = u"".join(random.choices(text_list,k=2))
                image = PutText.puttext(cv_image, text, point, font_path.as_posix(), font_size, color)
                Image.fromarray(image).save('generate_images/gen{}.jpg'.format(i))
    cv.imshow("sample", image)
    cv.waitKey(0)

if __name__ == '__main__':
    main()

