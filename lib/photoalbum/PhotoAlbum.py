### Description: Leiden Tech
### Category: Games
### License: MIT
### Appname: PhotoAlbum
### Built-in: no

import os
import badge
import ugfx
import machine
import random
import appglue
import time

def PhotoAlbum():
    badge.init()
    badge.eink_init()
    ugfx.set_lut(ugfx.GREYSCALE)
    ugfx.init()
    ugfx.input_init()
    ugfx.input_attach(ugfx.JOY_UP,lambda pressed: btn_up(pressed))
    ugfx.input_attach(ugfx.JOY_DOWN,lambda pressed: btn_down(pressed))
    ugfx.input_attach(ugfx.JOY_LEFT,lambda pressed: btn_left(pressed))
    ugfx.input_attach(ugfx.JOY_RIGHT,lambda pressed: btn_right(pressed))
    ugfx.input_attach(ugfx.BTN_SELECT,lambda pressed: btn_select(pressed))
    ugfx.input_attach(ugfx.BTN_START,lambda pressed: btn_start(pressed))
    ugfx.input_attach(ugfx.BTN_A,lambda pressed: btn_a(pressed))
    ugfx.input_attach(ugfx.BTN_B,lambda pressed: btn_b(pressed))

    [year, month, mday, wday, hour, minute, second, microseconds] = machine.RTC().datetime()
    random.seed(int(microseconds))
    display()

def display():
    global font, fgcolor, imageNum, imageDir, images,imageList, sequenceMode, reloadMode, delay
    #clearbg()
    #It'd be nice to know the size of the image to get a center extract
    badge.eink_png(0,0,imageDir + "/" + images[imageNum - 1])
    badge.eink_busy_wait()
    ugfx.flush()
    timeStamp=time.time()

    if reloadMode is True:
        if sequenceMode is True:
            #stop the doubles
            newImageNum = random.randint(1,numImages)
            while newImageNum == imageNum:
                newImageNum = random.randint(1,numImages)
            imageNum = newImageNum
        else:
            imageNum = imageNum + 1
            if imageNum > numImages:
                imageNum = 1
        #time.sleep(delay) #Nope, sleep blocks the buttons
        now=time.time()
        first=True
        while now < ( timeStamp + delay ): #This is also blocking?!
            now=time.time()
            if pressed and not first:
                break
            first=False
        display()

def quit():
    global font,bgcolor,fgcolor
    clearbg()
    ugfx.string(50, 50, "Quitting", font,fgcolor)
    ugfx.flush()
    appglue.start_app("launcher",False)

def clearfg():
    global font,bgcolor,fgcolor
    ugfx.clear(fgcolor)
    ugfx.flush()
    
def clearbg():
    global font,bgcolor,fgcolor
    ugfx.clear(bgcolor)
    ugfx.flush()

def clearScreen():
    clearfg()
    clearbg()

def btn_a(pressed):
    global reloadMode
    if pressed:
        reloadMode=False
        display()

def btn_b(pressed):
    global reloadMode
    if pressed:
        reloadMode=True
        display()

def btn_up(pressed):
    global numImages, imageNum, sequenceMode, reloadMode
    if pressed:
        sequenceMode=True
        reloadMode=True #sequence mode is useless if not in reload mode
        newImageNum = imageNum+1
        if newImageNum > numImages:
            newImageNum= 1
        imageNum = newImageNum
        display()

def btn_down(pressed):
    global numImages, imageNum, sequenceMode, reloadMode
    if pressed:
        sequenceMode=False
        reloadMode=False

def btn_left(pressed):
    global imageNum, sequenceMode, numImages
    sequenceMode=False
    if pressed:
        if imageNum > 1:
            imageNum=imageNum-1
        else:
            if imageNum == 1:
                imageNum=numImages;
        display()

def btn_right(pressed):
    global numImages, imageNum, sequenceMode
    if pressed:
        if imageNum < numImages:
            sequenceMode=False
            imageNum=imageNum+1
        else:
            if imageNum == numImages:
                imageNum=1
        display()

def btn_start(pressed):
    if pressed:
        quit()

def btn_select(pressed):
    if pressed:
        global font,bgcolor,fgcolor
        clearbg()
        ugfx.string(50, 50, "Restarting", font,fgcolor)
        ugfx.flush()
        appglue.start_app("PhotoAlbum",False)

########
# MAIN #
########
#Any way to upload?
bgcolor=ugfx.WHITE
fgcolor=ugfx.BLACK
font="PermanentMarker22"
delay=4

#random Mode means it reloads the an image randomly every delay seconds
sequenceMode=False

#If set to true will loop through images (or randomly choose if above is set) - if set to false will stay on the image
reloadMode=False

imageNum=1

#try sdcard dir first then switch to local media
imageDir="/sdcard/PhotoAlbum"
try:
    #hmmm, if the problem is that the /sdcard dir doesn't exist we probably should make it here - but then, which exception should I be looking for?
    badge.mount_sdcard()
except:
    #Any way of knowing what the app root dir is? getcwd() is always '/' as far as I can tell
    imageDir="/lib/PhotoAlbum"

imageList = os.listdir(imageDir)
images = []
#cleanup to only use png images
for image in imageList:
    clearbg()
    iSplit =  image.split('.') #Love to have a strstr here
    splitLen = len(iSplit) - 1
    ext = iSplit[splitLen]
    if ext == "png" or ext == "PNG": #should be a png then.
        images.append(image)

numImages=len(images)

if numImages == 0:
    ugfx.string(50, 0, "ERROR: NO IMAGES FOUND!", font,fgcolor)
    ugfx.flush()
    time.sleep(2)
    quit()

PhotoAlbum()
