import os
import sys
from PIL import Image

def list_images():
    imgs = {}
    os.chdir('./input img')
    print("These are the images loaded in the folder:")
    for cur, dirs, files in os.walk(os.curdir):
        for i, file in enumerate(files):
            if os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1]  == '.png':
                print(f'{i} - {file}')
                imgs[i] = file
        print(f'{len(files)} - Resize all images')
        print(f'{len(files) + 1} - Exit')
        selection = get_desired_selection(files)
        if selection == len(files) + 1:
            raise(KeyboardInterrupt)
        os.chdir('..')
        return imgs, selection


def get_desired_selection(files):
    while 1:
        selection = input("Please select an option to continue: ")
        try: 
            selection = int(selection)
            if selection < 0 or selection > len(files) + 1:
                raise(ValueError)
            break
        except ValueError:
            print("Invalid value!")
    return selection   


def get_desired_size():
    width_size = input("Input a width size (in px). Height will be automatically applied: ")
    while 1:
        try:
            width_size = int(width_size)
            break
        except ValueError:
            print("Invalid value!")
    return width_size


def resize(file, width_size):
    img = Image.open(f'./input img/{file}')
    width_pc = (width_size/float(img.size[0]))
    height_size = int((float(img.size[1])*float(width_pc)))
    img = img.resize((width_size,height_size), Image.ANTIALIAS)
    return img    


def main():
    imgs, selection = list_images()
    width_size = get_desired_size()
    if selection == len(imgs.items()):
        for file in imgs.values():
            try:
                img = resize(file, width_size)
                img.save(f'{os.curdir}/output img/{file}')
            except:
                print(f"Error saving the image: {file}")
    else:
        try: 
            img = resize(imgs[selection], width_size)
            img.save(f'{os.curdir}/output img/{imgs[selection]}')
        except:
            print(f"Error saving the image: {imgs[selection]}")
    os.chdir('./output img')
    print(f"Images succesfully saved at: {os.getcwd()}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo...')
        sys.exit()