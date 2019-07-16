from PIL import Image

def main():
    # Q1: word_index_count
    with open("./words.txt", 'r') as textfile:
        text = textfile.read()
        arr_words = text.split()
        mp = {} #{string:int}
        for word in arr_words:
            if word in mp:
                mp[word] += 1
            else:
                mp[word] = 1

    with open("Q1.txt", 'a') as savefile:
        i = 0
        for key, value in mp.items():
            if i != len(mp) - 1:
                savefile.write("{word} {index} {count}\n".format(word=key, index=i, count=value))
                i += 1
            else:
                savefile.write("{word} {index} {count}".format(word=key, index=i, count=value))
                
                

            
    # Q2
    filename = "./westbrook.jpg"
    img1 = Image.open(filename)
    img1.show()
    img2 = Image.eval(img1, lambda pixel: pixel//2)
    img2.show()
    img2.save("Q2.jpg")



if __name__ == '__main__':
    main()
