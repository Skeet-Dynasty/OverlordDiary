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

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Переход между экранами игрового меню.

define config.intra_transition = dissolve


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = None


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = None


define config.window = "auto"


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


default preferences.text_cps = 75
default preferences.afm_time = 15


define config.save_directory = None

define config.window_icon = "gui/window_icon.png"
