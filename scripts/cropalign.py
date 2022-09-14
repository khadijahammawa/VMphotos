#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:36:01 2021

@author: NatalieRotstein Feb 15th 2022
"""
#import modules
import numpy
import cv2 
#create the dictionaries where the image info and data are saved
imginfo=[{"name":"1"},{"name":"2"},{"name":"3"},{"name":"4"},
         {"name":"11"},{"name":"12"},{"name":"13"},{"name":"14"}]
imgdata=[{"name":"1"},{"name":"2"},{"name":"3"},{"name":"4"},
         {"name":"11"},{"name":"12"},{"name":"13"},{"name":"14"}]
cfall=numpy.zeros(8) ##SWITCH OUT LATER

##SHOW THE INSTRUCTION IMAGE
instrfile="E:/CAMH/vismod/VMphotos/scripts/textimgs/PupilLocationInstr.jpg"
instr=cv2.imread(instrfile)
cv2.imshow('image', instr)
cv2.waitKey(0)

#cfall=numpy.zeros(4) #this is for when testing w just 4 images
# function to display the coordinates of the points clicked on the image  
def click_event(event, x, y, flags, params): 
    global ix,iy
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates on the Shell 
        print(x, ' ', y) 
        ix,iy=x,y
        # displaying the coordinates on the image window 
        radius=30
        cv2.circle(img, (x,y), radius, (255,0,0), 2)
        #font = cv2.FONT_HERSHEY_SIMPLEX 
        #cv2.putText(img, str(x) + ',' +
        #            str(y), (x,y), font, 
        #            1, (255, 0, 0), 2)
        cv2.imshow('image', img)
  

    
for n in range(0,len(imginfo)):

    filebase="E:/CAMH/vismod/VMphotos/improc/bgremoved/"

    #ext=".jpg"
    ext=".png"
    file=filebase + imginfo[n]["name"] + ext
    imginfo[n]["file"]=file
    print("name of file: ",file)

    img = cv2.imread(file) 
    l = img.shape[0]
    w = img.shape[1]
    imgdata[n]["use"]=img
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # displaying the image
    cv2.imshow('image', img)
  
    # setting mouse handler for the image and calling the click_event() function 
    print('set left eye location')
    cv2.setMouseCallback('image', click_event) 

    # wait for a key to be pressed to exit 
    key=cv2.waitKey(0)
    print(key)
    if key == ord('a'):
    #if key == 2:
        imginfo[n]["lx"]=ix
        imginfo[n]["ly"]=iy
    elif key == ord('d'):
    #elif key == 3:
        imginfo[n]["rx"]=ix
        imginfo[n]["ry"]=iy

    # close the window 
    cv2.destroyAllWindows() 
        
    #RERUN SAME IMAGE FOR OTHER EYE
    #img = cv2.imread(file) 
    #img=imgdata[n]["use"]

    #cv2.namedWindow('image', cv2.WINDOW_NORMAL)  
    # displaying the image 
    cv2.imshow('image', img)
    # setting mouse hadler for the image 
    # and calling the click_event() function 
    print('set right eye location')
    cv2.setMouseCallback('image', click_event) 

    # wait for a key to be pressed to exit 
    #cv2.waitKey(0) 
    key=cv2.waitKey(0)
    print(key)
    if key == ord('a'):
    #if key == 2:
        imginfo[n]["lx"]=ix
        imginfo[n]["ly"]=iy
    elif key == ord('d'):
    #elif key == 3:
        imginfo[n]["rx"]=ix
        imginfo[n]["ry"]=iy
    imginfo[n]["xdist"]=abs(imginfo[n]["rx"]-imginfo[n]["lx"])
    imginfo[n]["ydist"]=abs(imginfo[n]["ry"]-imginfo[n]["ly"])
    print()
    print(imginfo[n]["xdist"],imginfo[n]["ydist"])
    
    # # close the window 
    cv2.destroyAllWindows() 

print(imginfo)    
#if __name__=="__main__": 
#    main()

#########################################################################
## PART 2 - CALCULATE THE DISTANCES BETWEEN EYES IN THE VARIOUS IMAGES & DO IMAGE MANIPULATIONS BASED ON IT##
#########################################################################
print("RUNNING PART 2 - CALCULATIONS AND MANIPULATION OF IMAGES")
for n in range(0,len(imginfo)):
    cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
    img = cv2.imread(imginfo[n]["file"]) 
    imgdata[n]["orig"]=img
    #make local temp vars for easier use
    print("running image ",imginfo[n]["name"])
    rx=imginfo[n]["rx"]
    lx=imginfo[n]["lx"]
    ry=imginfo[n]["ry"]
    ly=imginfo[n]["ly"]
    origimg=imgdata[n]["orig"]
    
    ##do calculations
    xdist=abs(rx-lx)
    ydist=abs(ry-ly)
    xavg=(rx+lx)/2
    yavg=(ry+ly)/2
    xavg=int(xavg)
    yavg=int(yavg)
    cf=2.5 #crop factor: multiple of eyedist from center that image is cropped
    cropxmin=int(xavg-(cf*xdist))
    cropxmax=int(xavg+(cf*xdist))
    cropymin=int(yavg-(cf*xdist))
    cropymax=int(yavg+(cf*xdist))
    cfall[n]=cf

    
    ##UPDATED CROP CORRECTION
    ymax=origimg.shape[0]
    xmax=origimg.shape[1]
    #ZERO INDEX IS THE TOP OF ARRAY NOT BOTTOM!
    if cropymax>ymax: #if need space at bottom, need to reduce cf
        cropymax=ymax
        dist=cropymax-yavg        
        cfall[n]=dist/xdist

    if cropymin<0: #if need space at top of array, add black space
        dif=abs(cropymin)
        y=dif+2
        yavg=yavg+y
        blackarray=numpy.zeros((y,xmax,3),dtype=numpy.uint8)
        print("sizes would be image: ",origimg.shape,"blackarray: ",blackarray.shape)
        origimg=numpy.vstack((blackarray,origimg))
        imgdata[n]["orig"]=origimg
        #cv2.imshow('image2', origimg)
        #cv2.waitKey(0)
        #dont need to reset cfall bc just adding space to allow for crop
    imginfo[n]["xdist"]=xdist
    imginfo[n]["ydist"]=ydist
    imginfo[n]["xavg"]=xavg
    imginfo[n]["yavg"]=yavg
    cv2.destroyAllWindows() 


#NEXT STEP IS TO FIX LOOPS TO MATCH CF ACROSS ALL IMAGES
cf=min(cfall)
print("final crop factor is: ",cf)
for n in range(0,len(imginfo)):
    ##make sure to load all local variables from the array!!
    origimg=imgdata[n]["orig"]
    xdist=imginfo[n]["xdist"]
    ydist=imginfo[n]["ydist"]
    xavg=imginfo[n]["xavg"]
    yavg=imginfo[n]["yavg"]
    
    #THEN do the calculations
    cropxmin=int(xavg-(cf*xdist))
    cropxmax=int(xavg+(cf*xdist))
    cropymin=int(yavg-(cf*xdist))
    cropymax=int(yavg+(cf*xdist))
    #save the temp var values in the array
    imginfo[n]["cropxmin"]=cropxmin
    imginfo[n]["cropxmax"]=cropxmax
    imginfo[n]["cropymin"]=cropymin
    imginfo[n]["cropymax"]=cropymax

    cropped=origimg[cropymin:(cropymax + 1),cropxmin:(cropxmax + 1)]
    #cv2.imshow('image2', origimg)
    #cv2.waitKey(0)
    #cv2.imshow('image2', cropped)
    #cv2.waitKey(0)    
    resized=cv2.resize(cropped,(1000,1000), interpolation = cv2.INTER_CUBIC)
    imgdata[n]["cropped"]=cropped
    imgdata[n]["resized"]=resized

    
    #print(imginfo[n]["xdist"],imginfo[n]["ydist"],imginfo[n]["xavg"],imginfo[n]["yavg"])
##SHOW THE TEXT IMG
txtfile="C:/Users/feusn/Desktop/VMphotos/scripts/textimgs/ShowingCropAligned.jpg"
txtimg=cv2.imread(txtfile)
cv2.imshow('image', txtimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 


print("SHOWING FINAL IMAGES")
for n in range(0,len(imginfo)):
    #cv2.imshow('image', imgdata[n]["cropped"])
    cv2.imshow('image2', imgdata[n]["resized"])
    cv2.waitKey(0)
    
    filebase="C:/Users/feusn/Desktop/VMphotos/improc/aligned/"
    ext=".jpg"
    file=filebase + imginfo[n]["name"] + ext
    print("saving image",imginfo[n]["name"],"as",file)
    img = cv2.imwrite(file,imgdata[n]["resized"]) 
#print(imginfo)
