# SPONSORS APPLICATION
# SHOWN ONCE AFTER SETUP

import ugfx, badge, appglue, utime

def show_sponsors():
    for x in range(1, 8):
        ugfx.clear(ugfx.WHITE)
        ugfx.flush()
        try:
            badge.eink_png(0,0,'/lib/sponsors/sponsor%s.png' % x)
        except:
            ugfx.string(0, 0, "SPONSOR LOAD ERROR #"+str(x), "Roboto_Regular12", ugfx.BLACK)
        ugfx.flush()
        utime.sleep(4)

def program_main():
    print("--- SPONSORS APP ---")
    ugfx.init()
    ugfx.set_lut(ugfx.LUT_FULL)
    ugfx.clear(ugfx.BLACK)
    ugfx.flush()
    show_sponsors()
    appglue.start_app("") # Return home

# Start main application
program_main()