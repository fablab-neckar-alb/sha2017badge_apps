import utime, appglue, ugfx

err = "This resource package can not be started on it's own."

print(err)

ugfx.clear(ugfx.WHITE)
ugfx.string(0,0,err,"pixelade13", ugfx.BLACK)
ugfx.flush()

utime.sleep(5)
appglue.home()
