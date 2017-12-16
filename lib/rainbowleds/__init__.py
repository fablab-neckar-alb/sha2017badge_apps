import badge
import ugfx
import appglue

badge.init() 
ugfx.init()
badge.leds_init()
ugfx.input_init()

brightness = badge.nvs_get_u8("rainbowleds", "brightness", 20)
offset = badge.nvs_get_u8("rainbowleds", "offset", 0)

def main_menu(pushed):
    if(pushed):
        global brightness
        global offset
        badge.nvs_set_u8("rainbowleds", "brightness", brightness)
        badge.nvs_set_u8("rainbowleds", "offset", offset)
        appglue.home()

def brighter(pushed):
    if(pushed):
        global brightness
        brightness += 20
        if brightness > 255:
            brightness = 255
        create_colors()

def dimer(pushed):
    if(pushed):
        global brightness
        brightness -= 20
        if brightness < 5:
            brightness = 5
        create_colors()

def forward(pushed):
    if(pushed):
        global offset
        offset += 1
        if offset > 5:
            offset = 0
        create_colors()

def backward(pushed):
    if(pushed):
        global offset
        offset -= 1
        if offset < 0:
            offset = 5
        create_colors()

def create_colors():
    blue = bytes([0, 0, brightness, 0])
    cyan = bytes([brightness, 0, brightness, 0])
    green = bytes([brightness, 0, 0, 0])
    yellow = bytes([brightness, brightness, 0, 0])
    red = bytes([0, brightness, 0, 0])
    magenta = bytes([0, brightness, brightness, 0])
    rainbow = [blue, cyan, green, yellow, red, magenta]
    values = bytes()
    for i in range(6):
        i += offset
        if i > 5:
            i -= 6
        values += rainbow[i]
    badge.leds_send_data(values)


ugfx.set_lut(ugfx.LUT_NORMAL)

ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.flush()
ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.flush()

text = "colorful"
ugfx.string(190, 25, "STILL", "Roboto_BlackItalic24", ugfx.BLACK)
ugfx.string(170, 50, text, "PermanentMarker22", ugfx.BLACK)
length = ugfx.get_string_width(text, "PermanentMarker22")
ugfx.line(170, 72, 184 + length, 72, ugfx.BLACK)
ugfx.line(180 + length, 52, 180 + length, 70, ugfx.BLACK)
ugfx.string(180, 75, "Anyway", "Roboto_BlackItalic24", ugfx.BLACK)
ugfx.string(0, 110, "START: exit, UP/DOWN: brightness, LEFT/RIGHT: move", "Roboto_Regular12", ugfx.BLACK)
try:
    badge.eink_png(0, 40, '/lib/rainbowleds/icon.png')
except:
    ugfx.string(100, 50, "Error loading icon.png", ugfx.BLACK)

ugfx.flush()

badge.leds_enable()
create_colors()

ugfx.input_attach(ugfx.JOY_UP, brighter)
ugfx.input_attach(ugfx.JOY_DOWN, dimer)
ugfx.input_attach(ugfx.JOY_LEFT, backward)
ugfx.input_attach(ugfx.JOY_RIGHT, forward)
ugfx.input_attach(ugfx.BTN_START, main_menu)