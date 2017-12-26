import badge, ugfx
badge.init()
ugfx.init()

while True:
    for i in range(8):
        ugfx.clear(ugfx.WHITE)
        ugfx.display_image(int(ugfx.width()/2. - 62.5), int(ugfx.height()/2. - 62.5), "/lib/milliways/milliways{}.png".format(i))
        ugfx.flush()