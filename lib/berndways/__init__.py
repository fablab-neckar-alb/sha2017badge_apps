import badge, ugfx
badge.init()
ugfx.set_lut(ugfx.GREYSCALE)
ugfx.init()

while True:
    for i in range(15):
        badge.eink_png(0,0, "/lib/berndways/VulcanBernd{:X}.png".format(i))
        badge.eink_busy_wait()
        ugfx.flush()
