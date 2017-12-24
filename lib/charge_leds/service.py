import badge

def show_leds(nousb,forceval=None):
    if forceval is None:
        vDrop = badge.nvs_get_u16('splash', 'bat.volt.drop', 1000) - 1000
        bvol = badge.battery_volt_sense() + vDrop
        crg = badge.battery_charge_status()
        uvol = badge.usb_volt_sense()
    else:
        vDrop = 0
        bvol = forceval
        crg = True
        uvol = 5000
    bvolmin = badge.nvs_get_u16("batt","vmin",3500)
    bvolmax = badge.nvs_get_u16("batt","vmax",4100)
    bvolstg = (bvolmax - bvolmin)/6
    maxbrightness=32
    ledson = True
    if nousb and uvol < 4000:
        led_status = bytes([0]*24)
        ledson = False
    elif (uvol >= 4000 and not crg) or bvol >= bvolmax:
        led_status = bytes([maxbrightness, 0, 0, 0]*6)
    elif bvol <= bvolmin:
        led_status = bytes([0, maxbrightness, 0, 0]*6)
    else:
        use_led = int((bvol-bvolmin)/bvolstg)
        lb = maxbrightness
        crglvl = round(lb*((bvol-bvolmin)/bvolstg-use_led))
        led_status = bytes(
                     [0, maxbrightness,0,0] * (5-use_led) + 
                     [crglvl, lb-crglvl,0,0] +
                     [maxbrightness, 0,0,0] * use_led
                     )
    if ledson:
        badge.leds_enable()
    else:
        badge.leds_disable()
    badge.leds_send_data(led_status, 24)    

def loop():
    show_leds(True)
    if badge.usb_volt_sense() < 4000:
        return 300000
    else:
        return 1000

def setup():
    global loop
    if badge.nvs_get_u8("charge_leds", "enable", 0):
        badge.leds_init()
        badge.power_init()
    else:
        loop = lambda: 86400000
