from PIL import Image

# how to create a image with specified color

def main():
    size = height, width = 320, 200

    image1 = Image.new("RGB", size, "rgb(20, 100, 255)")

    image1.show()
    
    del image1



if ( __name__ == "__main__"):
    main()
