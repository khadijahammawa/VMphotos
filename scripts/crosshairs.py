#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:28:00 2021

@author: NatalieRotstein
"""


from PIL import Image
import numpy
import cv2 
  
def click_event(event, x, y, flags, params): 
    global ix,iy
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y) 
        ix,iy=x,y
        # displaying the coordinates 
        # on the image window 
        #radius=5
        radius=3
        cv2.circle(img, (x,y), radius, (255,0,0), 2)
        cv2.imshow('image', img)

####################################################################    
#### THIS SECTION DOES AUTOMATIC OVERLAY OF CROSSHAIR ON IMAGE #####
####################################################################
        
imginfo=[{"name":"1"},{"name":"2"},{"name":"3"},{"name":"4"},{"name":"5"},{"name":"6"},{"name":"7"},{"name":"8"},{"name":"11"},{"name":"12"},{"name":"13"},{"name":"14"},{"name":"15"},{"name":"16"},{"name":"17"},{"name":"18"}]
imgdata=[{"name":"1"},{"name":"2"},{"name":"3"},{"name":"4"},{"name":"5"},{"name":"6"},{"name":"7"},{"name":"8"},{"name":"11"},{"name":"12"},{"name":"13"},{"name":"14"},{"name":"15"},{"name":"16"},{"name":"17"},{"name":"18"}]

for n in range(0,len(imginfo)):
#setting up file path
    crosshair='/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/crosshair.png'
    inputdir="/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/natural/"
    outputdir="/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/VM/"
    ext=".jpg"
    infile=inputdir + imginfo[n]["name"] + ext
    imginfo[n]["infile"]=infile
    outfile=outputdir + imginfo[n]["name"] + ext
    imginfo[n]["outfile"]=outfile    
    print(infile)
#read in file & put crosshair onto it    
    img = cv2.imread(infile) 
    imgdata[n]["use"]=img
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)    
    background = Image.open(imginfo[n]["infile"])
    foreground = Image.open(crosshair)
    
#adjusts crosshair location for the images taken at side angle
    if imginfo[n]["name"] in {"2","12"}:
        x=6
    elif imginfo[n]["name"] in {"3","13"}:
        x=-2
    else:
        x=2
    y=2

#put crosshair onto image at predetermined coordinates, then save
    background.paste(foreground, (x, y), foreground)
    background.save(imginfo[n]["outfile"])
    VM=cv2.imread(imginfo[n]["outfile"])
#resize image before showing for the sake of better visibility
    cv2.resize(VM,(600,600))
    cv2.imshow('image',VM)
    
#THIS SECTION ALLOWS FOR YOU TO MANUALLY SELECT CROSSHAIR LOCATION
#HAVE IT SHOW THE NEW IMAGE SO YOU CAN SEE RELATIVE TO CURRENT CROSSHAIR 
    key2=cv2.waitKey(0)
    print(key2)
    
    if key2==109: ## m key -> SWITCH TO MANUAL ALIGNMENT
    #import the image (so it goes back to 300x300 not 600x600)
        img = cv2.imread(imginfo[n]["outfile"])
        # displaying the image 
        cv2.imshow('image', img)
        print('set new crosshair location')
        cv2.setMouseCallback('image', click_event)
    #if pressed right arrow, record coordinates
        cv2.waitKey(0)
        imginfo[n]["x"]=ix
        imginfo[n]["y"]=iy
    # close the window 
        cv2.destroyAllWindows()
    
    #calculate distance from center
        imginfo[n]["xdist"]=imginfo[n]["x"]-147
        imginfo[n]["ydist"]=imginfo[n]["y"]-147
        x=imginfo[n]["xdist"]
        y=imginfo[n]["ydist"]
        print(x,y)
        
        background = Image.open(imginfo[n]["infile"])
        foreground = Image.open(crosshair)
    
    #put the crosshair onto the face image and then save it
        background.paste(foreground, (x, y), foreground)
        background.save(imginfo[n]["outfile"])
        VM=cv2.imread(imginfo[n]["outfile"])
        
    #show the updated image
        cv2.imshow('image',VM)
        cv2.waitKey(0)
    

  