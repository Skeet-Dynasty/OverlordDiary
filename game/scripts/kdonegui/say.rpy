# KDONE GUI
# TEXTBOX SCREEN
# MADE BY @b3rg3n
# Since 2025 (c)
init python:

    showstatus = True
    pps = 2
    status_name = ""
    status_color = "#fff"
    status_color_custom = "#fff"
    def kdone_status():
        global status_name
        global status_color
        global status_color_custom
        if not showstatus or pps <= 0:
            status_name = ""
            status_color = status_color_custom or "#ffffff"
        elif pps == 1: #Белый
            status_name = "Состояние: Стабильное"
            status_color = "#ffffff"
            status_color_custom = "#ffffff"
        elif pps == 2: #Красный
            status_name = "Состояние: Обострение"
            status_color = "#ff0000"
            status_color_custom = "#ffffff"
        elif pps == 3: #Зелёный
            status_name = "Состояние: Радость"
            status_color = "#00ff00"
            status_color_custom = "#ffffff"

    while kdone_status in config.window_overlay_functions:
        config.window_overlay_functions.remove(kdone_status)
    config.window_overlay_functions.append(kdone_status)


screen say(who, what):
    style_prefix "say"

    if showstatus and pps > 0:
        add im.MatrixColor("gui/dialogue_box/status.webp", im.matrix.colorize("#000", status_color)):
            xpos 1104
            ypos 871
        text status_name:
            xpos 1162
            ypos 875
            size 20
        if kdone_invent_dostup:
            imagebutton:
                idle im.MatrixColor("gui/dialogue_box/inventory.webp", im.matrix.colorize("#000", status_color))
                hover im.MatrixColor("gui/dialogue_box/inventory_hover.webp", im.matrix.colorize("#000", status_color))
                xpos 534
                ypos 871
                activate_sound start_m
                hover_sound select_m
                action ShowMenu("kdone_inventory")
            text "Пошарить по карманам":
                xpos 592
                ypos 875
                size 20

    imagebutton:
        idle im.MatrixColor("gui/dialogue_box/backward_idle.webp", im.matrix.colorize("#000", status_color))
        hover im.MatrixColor("gui/dialogue_box/backward_hover.webp", im.matrix.colorize("#000", status_color))
        xpos 38
        ypos 924
        activate_sound start_m
        hover_sound select_m
        action Rollback()#ShowMenu("help")
    add im.MatrixColor("gui/dialogue_box/dialogue_box_large.webp", im.matrix.colorize("#000", status_color)):
        xpos 174
        ypos 866
    imagebutton:
        idle im.MatrixColor("gui/dialogue_box/hide_idle.webp", im.matrix.colorize("#000", status_color))
        hover im.MatrixColor("gui/dialogue_box/hide_hover.webp", im.matrix.colorize("#000", status_color))
        xpos 1508
        ypos 883
        activate_sound start_m
        hover_sound select_m
        action HideInterface()
    if not config.skipping:
        imagebutton:
            idle im.MatrixColor("gui/dialogue_box/forward_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("gui/dialogue_box/forward_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1768
            ypos 924
            activate_sound start_m
            hover_sound select_m
            action Skip()
    else:
        imagebutton:
            idle im.MatrixColor("gui/dialogue_box/fast_forward_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("gui/dialogue_box/fast_forward_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1768
            ypos 924
            activate_sound start_m
            hover_sound select_m
            action Skip()
    text what:
        id "what"
        xpos 194
        ypos 914
        xmaximum 1541
        size 35
        line_spacing 1
    if who:
        text who:
            id "who"
            xpos 194
            ypos 894
            size 35
            line_spacing 1

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
