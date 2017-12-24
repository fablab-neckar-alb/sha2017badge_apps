# TODO
# exiting

import ugfx, network, wifi, badge, time, dialogs
from umqtt.simple import MQTTClient

font_height = 16
text_padding = 2
header_text = '#sha2017 @ chat.freenode.org'
nick = badge.nvs_get_str('owner', 'name', 'AcidPhreak')
program_name = 'shairc'
buffer_len = 21
message_li = []

def wifi_up():
  wifi.init()
  while not wifi.sta_if.isconnected():
    time.sleep(0.1)
    pass
  return wifi.sta_if.ifconfig()[0]

def showSplash():
  clearGhosting()
  ugfx.clear(ugfx.WHITE)
  ugfx.string(100,50,'IRC @ SHA IIRC','Roboto_Regular18',ugfx.BLACK)
  ugfx.flush()
  time.sleep(2)
  print('splash done')
  clearGhosting()
  ugfx.clear(ugfx.WHITE)

def clearGhosting():
  ugfx.clear(ugfx.WHITE)
  ugfx.flush()
  badge.eink_busy_wait()
  ugfx.clear(ugfx.BLACK)
  ugfx.flush()
  badge.eink_busy_wait()

def onMessage(topic, msg):
  if (message_list.count() > buffer_len):
    remove_item(buffer_len)
  message_li.insert(0, msg)
  redraw_list()

def redraw_list():
  while (message_list.count() > 0):
    message_list.remove_item(0)
  for msg in message_li:
    message_list.add_item(msg)

#def connectClick(pushed):
#  if pushed:
#    print('hello world')
    #selected = options.selected_text().encode()
    #print('selected')
    #options.destroy()

    #badge.eink_busy_wait()
    #deepsleep.start_sleeping(1)

    #print(ssidList.index(selected))
    #ugfx.clear(ugfx.WHITE)
    #ugfx.string(100,50,selected,'Roboto_Regular18',ugfx.BLACK)
    #ugfx.flush()

    #badge.nvs_set_str("badge", "wifi.ssid", selected)
#  else:
#    print('nah')

def show_message_prompt(pushed):
  mqtt.publish("irc/shabadge/message/sshow/fjas",
               "!say %s: %s" % (nick,
                                dialogs.prompt_text("Message:")))
  ugfx.flush()

def __main__():
    global mqtt, message_list
    badge.init()
    ugfx.init()
    ugfx.input_init()

    wifi_up()

    import random
    badgeid = str(random.randint(0,5000000))
    mqtt = MQTTClient(badgeid, "185.35.202.211", 1337, "alarm", "alarm") # internet of shit
    mqtt.connect()
    mqtt.set_callback(onMessage)

    mqtt.subscribe("irc/shabadge/message/#")

    #showSplash()

    # Write header text
    ugfx.string(text_padding, text_padding, header_text, 'Roboto_Regular%d' % font_height, ugfx.BLACK)

    # Draw message window
    message_list = ugfx.List(0, font_height, ugfx.width(), ugfx.height() - font_height)
    message_list.set_focus()

    # Input bindings
    ugfx.input_attach(ugfx.BTN_A, show_message_prompt)
    #ugfx.input_attach(ugfx.BTN_B, connectClick)
    ugfx.input_attach(ugfx.JOY_UP, lambda pushed: ugfx.flush() if pushed else 0)
    ugfx.input_attach(ugfx.JOY_DOWN, lambda pushed: ugfx.flush() if pushed else 0)

    # Bootstrapping
    ugfx.set_lut(ugfx.LUT_FULL)
    ugfx.flush()
    ugfx.set_lut(ugfx.LUT_FASTER)

    while True:
        mqtt.wait_msg()

__main__()


