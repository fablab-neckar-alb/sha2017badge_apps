import ugfx,badge,appglue,time
from charge_leds import service

ns="charge_leds"
svck="enable"


def get_svc_status():
    return badge.nvs_get_u8(ns, svck, 0)

def draw():
    ugfx.clear()
    ststring = "disable" if get_svc_status() else "enable"
    ugfx.string(0, 25, "START: main menu",  "Roboto_BlackItalic24", ugfx.BLACK)
    ugfx.string(0, 50, "SELECT: "+ststring+" service", "Roboto_BlackItalic24",  ugfx.BLACK)
    ugfx.flush()

def change_service():
    badge.nvs_set_u8(ns, svck, not get_svc_status())

def btn_change(pushed):
    if pushed:
        change_service()
        draw()

def btn_home(pushed):
    if pushed:
        appglue.home()

def btn_test(pushed):
    global testing
    if pushed:
        testing = True
        ugfx.clear()
        ugfx.demo("TESTING")
        ugfx.flush()
        for i in range(badge.nvs_get_u16("batt","vmin",3500),badge.nvs_get_u16("batt","vmax",4100)+25,25):
            service.show_leds(False,i)
            time.sleep(0.1)
        service.show_leds(False)
        ugfx.clear()
        vDrop = badge.nvs_get_u16('splash', 'bat.volt.drop', 1000) - 1000
        ugfx.string(0, 10, "VBat: "+str(badge.battery_volt_sense()+vDrop),  "Roboto_BlackItalic24", ugfx.BLACK)
        ugfx.string(0, 35, "VUSB: "+str(badge.usb_volt_sense()), "Roboto_BlackItalic24",  ugfx.BLACK)
        ugfx.string(0, 60, "CHRG: "+("YES" if badge.battery_charge_status() else "NO"), "Roboto_BlackItalic24",  ugfx.BLACK)
        ugfx.string(0, 85, "Done in 5 seconds", "Roboto_BlackItalic24",  ugfx.BLACK)
        ugfx.flush()
        badge.eink_busy_wait()
        time.sleep(5)
        testing = False
        draw()

def main():
    global testing
    testing = False
    badge.init()
    ugfx.init()
    ugfx.input_init()
    ugfx.set_lut(ugfx.LUT_FULL)
    ugfx.input_attach(ugfx.BTN_SELECT, btn_change)
    ugfx.input_attach(ugfx.BTN_START, btn_home)
    ugfx.input_attach(ugfx.BTN_FLASH, btn_test)
    draw()
    while True:
        if not testing:
            service.show_leds(False)


if __name__ == 'charge_leds':
    main()
