#!/bin/bash
#THIS SCRIPT RUNS ALL THE IMAGE PROCESSING SCRIPTS FOR VISMOD R01
#clear out the folders with things from prior subjects

cd /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/scripts
echo "Present working directory"
echo pwd

rm /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/aligned/*
rm /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/bgremoved/*
rm /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/matchbright/*
mkdir /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/matchbright/tmp
rm /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/natural/*
rm /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/VM/*
rm /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/orig/*
echo "enter subject ID"
read subid
cp /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/$subid/original/* /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/orig
ls /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/*/*

#first script makes photoshop & the remove-bg.jsx script run via terminal
python runPS.py
echo 'background removed from images'

#this script aligns the eyes and crops image to square
python cropalign.py
echo 'images are cropped'

#this script adjusts the brightness of image to appropriate range
python adjust_brightness.py
echo 'brightness adjusted'

#this script creates the scramble images
matlab -nodisplay -nosplash -nodesktop -r "CreatePhaseScramble; exit"
#matlab -nojvm -nodesktop -r 'try; CreatePhaseScramble; catch; end; quit'
echo 'natural images created'

#this script creates the visual modulation images with crosshairs
python crosshairs.py
echo 'VM images created'

cp -r /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/VM /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/$subid/
cp -r /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/improc/natural /c/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/$subid/

echo "stimuli creation complete"
