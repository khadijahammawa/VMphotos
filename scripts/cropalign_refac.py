#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import cv2

class ImageProcessor:
    def __init__(self, imginfo, imgdata):
        self.imginfo = imginfo
        self.imgdata = imgdata
        self.cfall = numpy.zeros(8)
        
    def display_instructions(self):
        instrfile = "C:/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/scripts/textimgs/PupilLocationInstr.jpg"
        instr = cv2.imread(instrfile)
        cv2.imshow('Instructions', instr)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def click_event(self, event, x, y, flags, params): 
        if event == cv2.EVENT_LBUTTONDOWN: 
            print(x, ' ', y) 
            self.ix, self.iy = x, y
            radius = 30
            cv2.circle(self.img, (x, y), radius, (255, 0, 0), 2)
            cv2.imshow('image', self.img) 
    
    def process_images(self, imginfo):
        filebase = "C:/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/bgremoved/"
        ext = ".png"
        
        for n in range(0, len(self.imginfo)):
            file = filebase + self.imginfo[n]["name"] + ext
            self.imginfo[n]["file"] = file
            print("name of file: ", file)
            
            self.img = cv2.imread(file) 
            self.l = self.img.shape[0]
            self.w = self.img.shape[1]
            self.imgdata[n]["use"] = self.img
            
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.imshow('image', self.img)
            print('set left eye location')
            cv2.setMouseCallback('image', self.click_event) 
            
            key = cv2.waitKey(0)
            print(key)
            if key == ord('a'):
                self.imginfo[n]["lx"] = self.ix
                self.imginfo[n]["ly"] = self.iy
            elif key == ord('d'):
                self.imginfo[n]["rx"] = self.ix
                self.imginfo[n]["ry"] = self.iy
                
            cv2.destroyAllWindows() 
            
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.imshow('image', self.img)
            print('set right eye location')
            cv2.setMouseCallback('image', self.click_event) 
        
            key = cv2.waitKey(0)
            print(key)
            if key == ord('a'):
                self.imginfo[n]["lx"] = self.ix
                self.imginfo[n]["ly"] = self.iy
            elif key == ord('d'):
                self.imginfo[n]["rx"] = self.ix
                self.imginfo[n]["ry"] = self.iy
            
        imginfo[n]["xdist"]=abs(imginfo[n]["rx"]-imginfo[n]["lx"])
        imginfo[n]["ydist"]=abs(imginfo[n]["ry"]-imginfo[n]["ly"])
        print()
        print(imginfo[n]["xdist"],imginfo[n]["ydist"])
    
        # # close the window 
        cv2.destroyAllWindows()
        print(imginfo)

