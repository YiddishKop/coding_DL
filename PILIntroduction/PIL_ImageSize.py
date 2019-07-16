from PIL import Image

def main():
    filename = "d:/YID_git_repos/DLCoding/naruto1.jpg"

    image = Image.open(filename)

    print(image.size)

if __name__ == '__main__':
    main()
