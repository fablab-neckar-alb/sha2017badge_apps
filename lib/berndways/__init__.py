import badge, ugfx
badge.init()
ugfx.set_lut(ugfx.GREYSCALE)
ugfx.init()

while True:
    for i in range(15):
        ugfx.clear(ugfx.WHITE)
        ugfx.display_image(0,0, "/lib/photoalbum/VulcanBernd{:X}.png".format(i))
        ugfx.flush()
