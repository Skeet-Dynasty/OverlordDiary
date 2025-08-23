label start:
    stop music fadeout 2
    scene black
    with Fade(1.2, 1.5, 1.0)
    pause 0.5
    jump kdone_carter_prologue

label splashscreen:
    $ renpy.movie_cutscene("source/videosos/zastavka.ogv")
    return

label main_menu:
    play music ne_lubov fadein 4
    scene kdone_menu
    with Fade(1.5, 1.2, 1.0)
    show ifone:
        xpos(0.05) ypos(1.3)
        linear 1 xpos(0.05) ypos(0.3)
    $ kdone.p(2)
    call screen main_menu