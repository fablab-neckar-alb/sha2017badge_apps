###Lights Egg
### Author: f0x
### License: GPLv3

## A flashlight app which does red and white light, and allows you to change the brightness

import badge, ugfx, appglue
badge.leds_enable()
ugfx.input_init()
ugfx.init()

on = False
night_mode = False
brightness = 0

def draw_text():
    ugfx.clear(ugfx.WHITE)
    ugfx.string(20, 20,  "Night Mode: " + str(night_mode), "Roboto_Regular18", ugfx.BLACK)
    ugfx.string(20, 40,  "Brightness: " + str(brightness), "Roboto_Regular18", ugfx.BLACK)
    ugfx.string(20, 65,  "up/down: brightness", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(20, 80,  "left/right: night mode", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(20, 95,  "A/flash:    toggle", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(20, 110, "B:          back to home", "Roboto_Regular12", ugfx.BLACK)
    ugfx.flush()

def home(pressed):
  if pressed:
    appglue.home()

def brightness_up(pressed):
    global brightness
    global on
    if pressed:
        brightness = brightness + 1
    if brightness > 5:
        brightness = 5
    on = not on
    print(brightness)
    toggle(True)

def brightness_down(pressed):
    global brightness
    global on
    if pressed:
        brightness = brightness - 1
    if brightness < 0:
        brightness = 0
    on = not on
    print(brightness)
    toggle(True)


def toggle(pressed):
    global on
    draw_text()
    if pressed:
        if on:
            on = False
            badge.leds_send_data(''.join(['\0' for i in range(24)]), 24)
            print("off")
        else :
            on = True
            if night_mode:
                if brightness == 0:
                    badge.leds_send_data(''.join(['\0\5\0\0' for i in range(6)]), 24)
                elif brightness == 1:
                    badge.leds_send_data(''.join(['\0\25\0\0' for i in range(6)]), 24)
                elif brightness == 2:
                    badge.leds_send_data(''.join(['\0\45\0\0' for i in range(6)]), 24)
                elif brightness == 3:
                    badge.leds_send_data(''.join(['\0\75\0\0' for i in range(6)]), 24)
                elif brightness == 4:
                    badge.leds_send_data(''.join(['\0\100\0\0' for i in range(6)]), 24)
                elif brightness == 5:
                    badge.leds_send_data(''.join(['\0\177\0\0' for i in range(6)]), 24)
            else:
                if brightness == 0:
                    badge.leds_send_data(''.join(['\5' for i in range(24)]), 24)
                elif brightness == 1:
                    badge.leds_send_data(''.join(['\25' for i in range(24)]), 24)
                elif brightness == 2:
                    badge.leds_send_data(''.join(['\45' for i in range(24)]), 24)
                elif brightness == 3:
                    badge.leds_send_data(''.join(['\75' for i in range(24)]), 24)
                elif brightness == 4:
                    badge.leds_send_data(''.join(['\100' for i in range(24)]), 24)
                elif brightness == 5:
                    badge.leds_send_data(''.join(['\177' for i in range(24)]), 24)

            print("on")

def mode(pressed):
    global on
    global night_mode
    if pressed:
        night_mode = not night_mode
        draw_text()
        on = not on
        toggle(True)

draw_text()
ugfx.input_attach(ugfx.BTN_A, toggle)
ugfx.input_attach(ugfx.BTN_B, home)
ugfx.input_attach(ugfx.BTN_FLASH, toggle)
ugfx.input_attach(ugfx.JOY_LEFT, mode)
ugfx.input_attach(ugfx.JOY_RIGHT, mode)
ugfx.input_attach(ugfx.JOY_UP, brightness_up)
ugfx.input_attach(ugfx.JOY_DOWN, brightness_down)