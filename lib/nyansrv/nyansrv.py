import ugfx, badge
import appglue

def action_home(pressed):
    if (pressed):
        appglue.start_app("")
        
        
def store():
    global nyanValue
    badge.nvs_set_u8('nyancat', 'brightness', nyanValue)
    
def load():
    global nyanValue
    nyanValue = badge.nvs_get_u8('nyancat', 'brightness', 0)
    
def action_more(pressed):
    if (pressed):
        global nyanValue
        nyanValue = nyanValue + 1
        if (nyanValue>255):
            nyanValue = 255
        else:
          store()
        draw()

def action_less(pressed):
    if (pressed):
        global nyanValue
        nyanValue = nyanValue - 1
        if (nyanValue<0):
            nyanValue = 0
        else:
          store()
        draw()

def draw():
    ugfx.clear(ugfx.WHITE)
    ugfx.string(0, 0, "Nyancat service", "PermanentMarker22", ugfx.BLACK)
    global nyanValue
    if (nyanValue>0):
        ugfx.string(0, 25, "Service is enabled ("+str(nyanValue)+")!", "Roboto_Regular12", ugfx.BLACK)
        ugfx.string(0, 38, "Press start to see it in action.", "Roboto_Regular12", ugfx.BLACK)
    else:
        ugfx.string(0, 25,  "Service is disabled!", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(0, 38+13*1, "UP: Brightness +", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(0, 38+13*2, "DOWN: Brightness -", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(0, 38+13*3, "START: Go to homescreen", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(0, 38+13*4, "(Set brightness to 0 to disable!)", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(0, 38+13*5, "Warning: drains battery!", "Roboto_Regular12", ugfx.BLACK)
    ugfx.set_lut(ugfx.LUT_FASTER)
    ugfx.flush()

def program_main():  
    ugfx.init()
    ugfx.input_init()   
    ugfx.input_attach(ugfx.BTN_START, action_home)
    ugfx.input_attach(ugfx.JOY_UP, action_more)
    ugfx.input_attach(ugfx.JOY_DOWN, action_less)
    load()
    draw()
          
# Start main application
program_main()
 

