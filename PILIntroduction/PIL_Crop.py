from PIL import Image

def main():
    filename = "d:/YID_git_repos/DLCoding/naruto1.jpg"
    
    image = Image.open(filename)

    image.crop((10, 10, 100, 100)).show()

if __name__ == '__main__':
    main()
