import ugfx, badge

interval = 36000000

def setup():
    pass

def loop():
    global interval
    enabled = badge.nvs_get_u8("kinky","enable", 0)
    if enabled:
        return 9999999999
    else:
        return 0

def draw(y):
    enabled = badge.nvs_get_u8("kinky","enable", 0)
    if enabled:
        kinkychoice = badge.nvs_get_str("kinky", "kinkychoice", "redheads")

        ugfx.clear(ugfx.BLACK)
        ugfx.flush()
        ugfx.clear(ugfx.WHITE)
        ugfx.flush()

        ugfx.string_box(0,10,296,26, "Still fucking", "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyCenter)
        ugfx.string_box(0,45,296,38, kinkychoice, "PermanentMarker36", ugfx.BLACK, ugfx.justifyCenter)
        ugfx.string_box(0,94,296,26, "Anyway", "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyCenter)
        ugfx.flush()
    
    return 0