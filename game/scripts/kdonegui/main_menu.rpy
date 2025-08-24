init:
    default persistent.set_zvuk_suka = False

label start:
    stop music fadeout 2
    scene black
    with Fade(1.2, 1.5, 1.0)
    pause 0.5
    if config.developer:
        "Выбери картер, ебанько."
        menu:
            "Пролог":
                jump kdone_carter_prologue
            "Первый":
                jump kdone_carter_one
    else:
        jump kdone_carter_prologue

label splashscreen:
    python:
        if not persistent.set_zvuk_suka:
            kdone_ss(1.0)
            kdone_mm(.6)
            kdone_aa(.4)
            persistent.set_zvuk_suka = True
        rpc_update("В игре", "Смотрит заставку", "logogovna")
        renpy.movie_cutscene("source/videosos/zastavka.ogv")
    return

label main_menu:
    $ rpc_update("В игре", "В главном меню", "logogovna")
    play music ne_lubov fadein 4
    scene kdone_menu
    with Fade(1.5, 1.2, 1.0)
    show ifone:
        xpos(0.05) ypos(1.3)
        linear 1 xpos(0.05) ypos(0.3)
    $ kdone.p(2)
    call screen main_menu


screen main_menu():

    tag menu

    textbutton _("Сойти с ума") text_color "#FFFFFF" align(0.075, 0.375) at main_menu_fade_anim action Start()

    textbutton _("Вспомнить") text_color "#FFFFFF" align(0.075, 0.45) at main_menu_fade_anim action ShowMenu("load")

    textbutton _("Настройки\nХакинтоша") text_color "#FFFFFF" align(0.075, 0.565) at main_menu_fade_anim action ShowMenu("preferences")

    textbutton _("Об игре") text_color "#FFFFFF" align(0.075, 0.65) at main_menu_fade_anim action ShowMenu("about")

    textbutton _("Сбежать\nв дурку") text_color "#FFFFFF" align(0.075, 0.75) at main_menu_fade_anim action Quit(confirm=not main_menu)
