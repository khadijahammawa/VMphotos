import os
from os import listdir
from os.path import isfile, join
import sys
import shutil
import cv2

from PIL import Image, ImageStat, ImageEnhance


# 1). Convert image to greyscale, return average pixel brightness.
def brightness1(im_file):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]


# 2). Convert image to greyscale, return RMS pixel brightness.
def brightness2(im_file):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    return stat.rms[0]


def adjustbrightness(im_file,out_dir,im_name):
    # read the image
    im = Image.open(im_file)
	# image brightness enhancer
    enhancer = ImageEnhance.Brightness(im)
    meanstat = brightness1(im_file)
    print('brightness 1: ', meanstat)
    count = 0
    #tempname="temp_"+im_name
    temp_file=os.path.join(out_dir,"tmp", im_name)
    out_file=os.path.join(out_dir, im_name)
    im.save(temp_file)
    # factor = 1 #gives original image
    while abs(meanstat - 45) > 0.5:
    ##if >47 or <43, do bigger adjustments
        if meanstat > 47:
            factor = 0.95  # darkens the image
            im_output = enhancer.enhance(factor)
            im_output.save(temp_file)

            meanstat = brightness1(temp_file)
            im = Image.open(temp_file)
            enhancer = ImageEnhance.Brightness(im)

        elif meanstat < 43:
            factor = 1.05  # brightens the image
            im_output = enhancer.enhance(factor)
            im_output.save(temp_file)

            meanstat = brightness1(temp_file)
            im = Image.open(temp_file)
            enhancer = ImageEnhance.Brightness(im)
        
    #if 43<x<44.5 // 45.5<x<47, smaller adjustments
        if meanstat > 45.5:
            factor = 0.97  # darkens the image
            im_output = enhancer.enhance(factor)
            im_output.save(temp_file)

            meanstat = brightness1(temp_file)
            im = Image.open(temp_file)
            enhancer = ImageEnhance.Brightness(im)
            
        elif meanstat < 44.5:
            factor = 1.03  # brightens the image
            im_output = enhancer.enhance(factor)
            im_output.save(temp_file)

            meanstat = brightness1(temp_file)
            im = Image.open(temp_file)
            enhancer = ImageEnhance.Brightness(im)
        
        
        count = count + 1

        print('brightness iteration ', count, ': ', meanstat)

	# copy tmp image for final step
    #shutil.copyfile(r'tmp.jpg', r'final.jpg')
    shutil.copyfile(temp_file, out_file)

def resize(in_img,out_img):
    print(in_img)
    img = cv2.imread(in_img) 
    print(img.shape)
    resized=cv2.resize(img,(300,300), interpolation = cv2.INTER_CUBIC)
    img = cv2.imwrite(out_img,resized)
    print("image resized")
    
def adjustbrightness_orig(im_file):
    # read the image
    im = Image.open(im_file)
	# image brightness enhancer
    enhancer = ImageEnhance.Brightness(im)
    meanstat = brightness1(im_file)
    print('brightness 1: ', meanstat)
    count = 0
    im.save('tmp.jpg')
    # factor = 1 #gives original image
    while abs(meanstat - 45) > 2:
        if meanstat > 47:
            #factor = 0.5  # darkens the image
            factor = 0.1  # darkens the image
            im_output = enhancer.enhance(factor)
            im_output.save('tmp.jpg')

            meanstat = brightness1('tmp.jpg')
            im = Image.open('tmp.jpg')
            enhancer = ImageEnhance.Brightness(im)

        elif meanstat < 43:
            #factor = 1.5  # brightens the image
            factor = 1.1  # brightens the image
            im_output = enhancer.enhance(factor)
            im_output.save('tmp.jpg')

            meanstat = brightness1('tmp.jpg')
            im = Image.open('tmp.jpg')
            enhancer = ImageEnhance.Brightness(im)

        count = count + 1

        print('brightness iteration ', count, ': ', meanstat)

	# copy tmp image for final step
    shutil.copyfile(r'tmp.jpg', r'final.jpg')


def main():
    #file_path = input("Enter path to folder with images to process: ")
    #save_path = input("Enter path to folder to save output images")
    file_path="/Users/feusn/Desktop/VMphotos/improc/aligned/"
    save_path="/Users/feusn/Desktop/VMphotos/improc/matchbright/"
    res_path="/Users/feusn/Desktop/VMphotos/improc/natural/"
    print('Adjusting Brightness of Images.')
    for f in listdir(file_path):
        if isfile(join(file_path, f)) and f.endswith(('.png', '.jpg', '.JPG')):
            full_path = os.path.join(file_path, f)
            save_bright = os.path.join(save_path, f)
            save_300 = os.path.join(res_path, f)
            # process the images
            adjustbrightness(full_path,save_path,f)
            resize(save_bright,save_300)

if __name__ == "__main__":
    sys.exit(main())
