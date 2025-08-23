init python:

    def reg_char(id, name, who_color, what_color = "#fff", pref = "", suf = ""):
        global Character
        gl = globals()
        
        gl[id] = Character( name, color=who_color, what_color=what_color, drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_prefix=pref, what_suffix=suf )

    reg_char("th", '', "#18FFEB", pref="«", suf="»")
    reg_char("skt", 'Дима Скит', "#008080")
    reg_char("ovr", 'Данила', "#0066ff")
    reg_char("lxrd", 'deadlylxrd', "#09ff00")
    reg_char("brg", 'BERGEN', "#ffae00")
    reg_char("batek", 'Валерий', "#00ffea")
    reg_char("valerkin_kent", "Серега", "#6e3430")
    reg_char("barishnya", "Барышня", "#ff9191")
    reg_char("sveta", "Света", "#ff9191")
    reg_char("maman", 'Маман', "#006eff")
    reg_char("nvlbazar", 'NVL', "#ff9191")

init:
    image kdone_menu = Movie(fps=60, size = (1920, 1080), play="source/videosos/kdone_menu.ogv")