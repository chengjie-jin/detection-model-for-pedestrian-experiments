import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        if (img!="exit"):
            try:
                image = Image.open(img)
            except:
                print('Open Error! Try again!')
                continue
            else:
                r_image = yolo.detect_image(image)
                r_image.show()
                r_image.save("_result.jpg",'jpeg')
        else:
            return
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    FLAGS = parser.parse_args()

    print("Image detection mode")
    detect_img(YOLO(**vars(FLAGS)))

