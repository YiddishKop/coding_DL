from PIL import Image

# Image.blend, Image.composite, img.paste

def main():
    filename1 = "d:/YID_git_repos/DLCoding/naruto1.jpg" 
    filename2 = "d:/YID_git_repos/DLCoding/naruto2.jpg" 

    img1 = Image.open(filename1, "r")
    img2 = Image.open(filename2, "r")

    size1 = w1, h1 = img1.size # 299*168
    size2 = w2, h2 = img2.size # 299*168

    mask_img = Image.new("L", (w1, h1), "#ff00ff")

    Image.blend(img1, img2, 0.5).show()

    Image.composite(img1, img2, mask_img).show()

    img1.paste("blue", (2, 2, 10, 10))
    img2.paste(mask_img, (0, 0, 299, 168))

    img1.show()
    img2.show()

    del img1, img2
if __name__ == "__main__":
    main()
