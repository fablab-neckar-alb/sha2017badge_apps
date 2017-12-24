import badge, ugfx, appglue
badge.leds_enable()
ugfx.input_init()
ugfx.init()

def draw_text():
    ugfx.clear(ugfx.WHITE)
    ugfx.string(20, 20,   "Still buzzing anyway", "PermanentMarker22", ugfx.BLACK)
    ugfx.string(20, 60,   "A:       buzz!!", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(20, 80,   "B:       back to home", "Roboto_Regular12", ugfx.BLACK)
    ugfx.flush()
    
def home(pressed):
  if pressed:
    appglue.home()
    
def buzz(pressed):
  if pressed:
    badge.vibrator_activate(0xFF)

draw_text()
ugfx.input_attach(ugfx.BTN_A, buzz)
ugfx.input_attach(ugfx.BTN_B, home)