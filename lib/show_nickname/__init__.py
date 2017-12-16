import ugfx, badge, easydraw, time, appglue

easydraw.msg("","Show nickname", True)

enabled = badge.nvs_get_u8("shownick","enable", 0)
if enabled:
    enabled = 0
    easydraw.msg("Show nickname disabled!")
else:
    enabled = 1
    easydraw.msg("Show nickname enabled!")
    easydraw.msg("Go back to the splash and wait...")
enabled = badge.nvs_set_u8("shownick","enable", enabled)

time.sleep(5)
appglue.home()
