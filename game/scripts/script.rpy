# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    e "Вы создали новую игру Ren'Py."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return

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