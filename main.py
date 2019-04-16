from PutText import PutText
from PIL import Image
import os
import cv2 as cv
import argparse
import random
from pathlib import Path
import csv
from os import listdir
import math


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_data_root", type=str, default="prepare_images")

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

    im_root_list = list(im_root_path.glob("[!.*]*"))
    for im_path in im_root_list:
        cv_image = cv.imread(im_path.as_posix())

        #import pdb;pdb.set_trace()

        font_root_path = Path("font")
        for fn, font_path in enumerate(list(font_root_path.glob("*"))):
            diag_size = math.sqrt(cv_image.shape[0]**2+cv_image.shape[1]**2)
            
            for i in range(10):
                point = tuple(random.choices(list(range(0, int(diag_size/2))), k=2))
                font_size = random.randrange(int(diag_size/100),int(diag_size/5), 5)
                color = tuple(random.choices(list(range(0, 255)), k=3))
                text = u"".join(random.choices(text_list,k=2))
                image = PutText.puttext(cv_image, text, point, font_path.as_posix(), font_size, color)
                Image.fromarray(image).save('generate_images/gen{}_{}.jpg'.format(i,im_path.as_posix().split('/')[-1].split('.')[0]))
    #cv.imshow("sample", image)
    #cv.waitKey(0)

if __name__ == '__main__':
    main()

