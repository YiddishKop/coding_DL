from PIL import Image

# how to open image as an Image object

def main():
    file_name = "c:/Users/Ersin/Downloads/westbrook.jpg"
    image = Image.open(file_name, "r")
    image.show()

    del image

if __name__ == '__main__':
    main()
