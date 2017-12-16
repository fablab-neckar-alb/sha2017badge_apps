import ugfx, badge

def setup():
    pass

def loop():
    return 0

def draw(y):
    return [9999999999, 0]

def draw_going_to_sleep(y):
    enabled = badge.nvs_get_u8("shownick","enable", 0)
    if enabled:
        nick = badge.nvs_get_str("owner", "name", 'Boy Zonderman')
        ugfx.clear(ugfx.BLACK)
        ugfx.flush()
        ugfx.clear(ugfx.WHITE)
        ugfx.flush()

        ugfx.string_box(0,10,296,26, "STILL", "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyCenter)
        ugfx.string_box(0,45,296,38, nick, "PermanentMarker36", ugfx.BLACK, ugfx.justifyCenter)
        ugfx.string_box(0,94,296,26, "Anyway", "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyCenter)

        #the line under the text
        str_len = ugfx.get_string_width(nick,"PermanentMarker36")
        line_begin = int((296-str_len)/2)
        line_end = str_len+line_begin
        ugfx.line(line_begin, 83, line_end, 83, ugfx.BLACK)

        #the cursor past the text
        cursor_pos = line_end+5
        ugfx.line(cursor_pos, 46, cursor_pos, 81, ugfx.BLACK)

        ugfx.flush(ugfx.LUT_FULL)
        ugfx.flush(ugfx.LUT_FULL)
        badge.eink_busy_wait() 
    return [9999999999, 0]
