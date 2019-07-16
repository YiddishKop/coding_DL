from PIL import Image

def main():
    filename = "d:/YID_git_repos/DLCoding/naruto1.jpg"
    img1 = Image.open(filename, "r")
    img1.convert("1").show()
    img1.convert("L").show()

    del img1

if __name__ == '__main__':
    main()
