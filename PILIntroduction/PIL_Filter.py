from PIL import Image
from PIL import ImageFilter

def main():
    filename = "d:/YID_git_repos/DLCoding/naruto1.jpg"

    image = Image.open(filename)

    image.filter(ImageFilter.CONTOUR).show()
    image.filter(ImageFilter.EMBOSS).show()
    image.filter(ImageFilter.FIND_EDGES).show()
    # image.filter(ImageFilter.CONTOUR).show()
    # image.filter(ImageFilter.CONTOUR).show()



if __name__ == '__main__':
    main()
