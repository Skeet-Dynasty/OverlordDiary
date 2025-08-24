define config.name = _("Overlord Diary")

define config.default_textshader = "zoom"
default preferences.gl_powersave = False
define config.developer = True
define config.version = "1.0"

define gui.about = _p("""
""")

define build.name = "OD"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Вход и выход в игровое меню.

define config.enter_transition = ImageDissolve("source/images/anim/transition/wipeleft.webp", 0.5, ramplen=64)
define config.exit_transition = ImageDissolve("source/images/anim/transition/wipeleft.webp", 0.5, ramplen=64)
define config.intra_transition = ImageDissolve("source/images/anim/transition/wipeleft.webp", 0.5, ramplen=64)
define config.after_load_transition = MultipleTransition([False, ImageDissolve("source/images/anim/transition/wipeleft.webp", 0.5, ramplen=64), Solid("#000"), Pause(0.25), Solid("#000"), ImageDissolve("source/images/anim/transition/wipeleft.webp", 0.5, ramplen=64), True])
define config.end_game_transition = Fade(1.5, 1, 2)
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

define config.window = "auto"


default preferences.text_cps = 75
default preferences.afm_time = 15


define config.save_directory = None

define config.window_icon = "gui/window_icon.png"
