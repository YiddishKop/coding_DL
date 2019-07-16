from PIL import Image

def main():

    filename = "d:/YID_git_repos/DLCoding/naruto1.jpg"

    image = Image.open(filename)

    Image.eval(image, lambda a: a+100 if a+100<255 else a+50).show()

    image2 = image.split()[-1]
    image3 = image.split()[-2]
    image4 = image.split()[-3]

    print(list(image.split()[-1]))

    image2.show()
    image3.show()
    image4.show()

    del image



    
def save_target_image(self,
                      source,
                      name,
                      x_offset, # the wanted most left index of image
                      y_offset, # the wanted most up index of image
                      x_size,   # the pixels from most left
                      y_size,   # the pixels from most up.
                      flip,
                      convert):

        m_img = Image.open(source)
        if x_size!=0 and y_size!=0:
            m_img = m_img.crop((x_offset, y_offset, x_offset + x_size, y_offset + y_size))
        if flip is True:
            m_img = m_img.transpose(Image.FLIP_LEFT_RIGHT)
        if convert is True:
            m_img.load()
            alpha = m_img.split()[- 1]
            m_img = m_img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
            mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
            m_img.paste(255, mask)
            m_img.save(join(self.emotedb_path, name) + ".png", transparency=255, optimize=True)
        else:
            m_img.save(join(self.emotedb_path, name) + ".png", optimize=True) 


            
if __name__ == '__main__':
    main()
