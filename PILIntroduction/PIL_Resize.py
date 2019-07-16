from PIL import Image

def main():
    filename = "d:/YID_git_repos/DLCoding/naruto1.jpg"

    img = Image.open(filename)

    size = w, h = img.size

    img.resize((w//4, h//4)).show()

    img.thumbnail((w//4,h//4))
    print(img.size)
    print(list(img.getdata()))

    img.thumbnail((w//4,h//4))
    print(img.size)
    print(list(img.getdata()))

if __name__ == "__main__":
    main()
