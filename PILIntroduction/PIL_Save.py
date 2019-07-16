from PIL import Image

# open image
im = Image.open("c:/Users/Ersin/Downloads/westbrook.jpg")

# get the height and width
height, width = im.size

# expansion or shrink image
im.thumbnail((height//3, width//3), 0.3)
im.save("c:/Users/Ersin/Downloads/westbrook_cache2.jpg")

# save or show image
im.show()
