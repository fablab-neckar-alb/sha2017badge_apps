import dialogs, badge, easydraw, time, appglue, ugfx

easydraw.msg("","kinky", True)

enabled = badge.nvs_get_u8("kinky","enable", 0)

if enabled:
    if dialogs.prompt_boolean("App active, want to disable?"):
        enabled = badge.nvs_set_u8("kinky","enable",0)
else:
    if dialogs.prompt_boolean("App disabled, want to enable?"):
        enabled = badge.nvs_set_u8("kinky","enable",1)

ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.flush()

if enabled:
    savedchoice = badge.nvs_get_str("kinky", "kinkychoice", "")
    kinkychoice = dialogs.prompt_text("What is your kink today?", savedchoice)
    if kinkychoice:
        badge.nvs_set_str("kinky", "kinkychoice", kinkychoice)

    ugfx.clear(ugfx.BLACK)
    ugfx.flush()
    ugfx.clear(ugfx.WHITE)
    ugfx.flush()

    easydraw.msg("Kinky successfully set up!")
    easydraw.msg("You will find what you're looking for! :)")
    easydraw.msg("Go back to the splash and wait...")


time.sleep(3)
appglue.home()