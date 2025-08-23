label kdone_carter_prologue:

    python:
        showstatus = False

    play music ya_poteryan fadein 3

    $ kdone.s(showscreens)

    "Где-то на Камчатке, лето 2003-го."
    "Среди местных бомжей происходит соревнование: <<Сдохни или умри>>."
    "Тот, кто не смог выжрать литров водяры больше, чем выжрал другой - убывает в <<аутсайдеры>> с продырявленным от реактивного дриста очком."
    "Но нас интересуют два отдельных индивида..."

    scene dom_overlorda_out
    show batek_overa
    with dissolve2

    batek "Ну и хули ты стоишь?"
    extend " Наливай давай,{w=0.2} бля!" with vpunch

    "Пролог с этой хуйнёй пока скипнем, я ебал, хуйня якась постная получаецца("

    window hide
    stop music
    scene black
    jump kdone_carter_one

label kdone_carter_one:

    python:
        showstatus = True
        pps = 1

    play music make_some_noize fadein 3

    $ kdone.s(showscreens)
    th "Ничто так не бодрит с утра, как чашечка, выбитая из коленного сустава."
    "Именно с такой идеей проснулся наш дорогой Оверпупсик."
    $ kdone.s(hidescreens)
    " {w=1.0}{nw}"

    scene komnata_overa_prison
    $ kdone.m(send_mesto_hands(0.1, 0.6, 1.5))
    show unblink

    $ kdone.p(1)