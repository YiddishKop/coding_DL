from PIL import Image

# difference of getcolors, getpixel, getdata

def main():
    filename = "d:/YID_git_repos/DLCoding/naruto1.jpg"
    image = Image.open(filename).crop((0,0,3,3))
    size = width, height = image.size

    print(image.getcolors( width*height))
    print(image.getpixel((2,2))         )
    print(list(image.getdata())         )
    

if __name__ == '__main__':
    main()
