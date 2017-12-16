# Nyancat as a service
# Renze Nicolai 2017

# FOR NEW API

import utime, badge, binascii

nyanCnt = 0
nyanLeds = []
nyanEnabled = 0
colorList = []

def hex_to_grbw_list(hex_str):
    r,g,b = binascii.unhexlify(hex_str)
    w = 0
    while (r>0) and (g>0) and (b>0):
        r = r - 1
        g = g - 1
        b = b - 1
        w = w + 1
    return [g,r,b,w]

white = hex_to_grbw_list("ffffff")
yellow = hex_to_grbw_list("fffc0b")
green = hex_to_grbw_list("5bff0b")
orange = hex_to_grbw_list("ffb70b")
red = hex_to_grbw_list("ff0b50")
blue = hex_to_grbw_list("330bff")

colorList = [white, yellow, green, orange, red, blue]

# This function gets called by the home application at boot
def setup():
    global nyanEnabled
    nyanEnabled = badge.nvs_get_u8('nyancat', 'brightness', 0)
    if (nyanEnabled<1):
        print("Nyancat: Disabled! Please enable in the app!")
    else:
        badge.leds_enable()
        global nyanLeds
        ledValue = [0,0,0,0]
        for i in range(0,6):
            nyanLeds.append(ledValue)
            
        global colorList
        for i in range(0,len(colorList)):
            colorList[i][0] = round(colorList[i][0] * (nyanEnabled/255))
            colorList[i][1] = round(colorList[i][1] * (nyanEnabled/255))
            colorList[i][2] = round(colorList[i][2] * (nyanEnabled/255))
            colorList[i][3] = round(colorList[i][3] * (nyanEnabled/255))

def loop():
    global nyanEnabled
    if (nyanEnabled>0):
        global nyanCnt
        global brVal
        global colorList
        nyanCnt = nyanCnt + 1
        if nyanCnt >= len(colorList):
            nyanCnt = 0
                        
        ledValue = colorList[nyanCnt]
        
        for i in range(0,5):
            nyanLeds[i] = nyanLeds[i+1]  
        nyanLeds[5] = ledValue
        output = []
        for i in range(0,6):
            output = output + nyanLeds[i]
        badge.leds_send_data(bytes(output),24)
        return badge.nvs_get_u8('nyancat', 'delay', 50)
    return 0
