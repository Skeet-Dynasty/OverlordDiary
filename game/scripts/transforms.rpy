# DREAMAN TRANSFORMS
# by @b3rg3n
# since 2025

init:
    transform load_anim: # АНИМАЦИЯ МЕНЮ ЗАГРУЗКИ
        zoom 0.4 alpha 0
        ease 0.5 zoom 1.0 alpha 1
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform main_menu_fade_anim:
        alpha 0
        ease 0.5 alpha 1
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform notify_anim: # АНИМАЦИЯ МЕНЮ ЗАГРУЗКИ
        on show:
            zoom 0.4 alpha 0 xpos 0.0
            linear .5 zoom 1.0 alpha 1 xpos 0.05
        on hide:
            linear .5 zoom 0.4 alpha 0 xpos 0.0

    transform hidescreens:
        xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
        ease 1.0 xpos 0.0 ypos 0.2 alpha 0.0

    transform showscreens:
        ypos 0.2 alpha 0.0 subpixel True
        ease 1.0 ypos 0.0 alpha 1.0

    transform null_scr:
        pause 0.01