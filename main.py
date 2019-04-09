from PutText import PutText
import cv2 as cv
from PIL import Image

def main():
    cv_image = cv.imread("sample.jpg")
#    import pdb;pdb.set_trace()
    font_path = './font/g_brushtappitsu_freeH.ttf'

    image = PutText.puttext(cv_image, u"けいちゃん", (30, 30), font_path, 60, (0, 0, 0))

    Image.fromarray(image).save('gen.jpg')
    cv.imshow("sample", image)
    cv.waitKey(0)

if __name__ == '__main__':
    main()

