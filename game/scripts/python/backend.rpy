# КАЛ ПОД КАПОТОМ
# MADE BY @b3rg3n
# Since 2025 (c)
# Skeet Dynasty

init -999 python:

    from os import path

    kdone_source = 'source/'
    kdone_mod_folder = kdone_source

    kdone_img = kdone_source + 'images/'
    kdone_zvuk = kdone_source + 'audio/'
    kdone_video = kdone_source + 'videosos/'
    kdone_font = kdone_source + 'fonts/'

    kdone_anim = kdone_img + 'anim/'

    kdone_uncolorize = None

    for file in renpy.list_files(): # ФУНКЦИЯ ГОПА АУДИО БЕЗ ДЕФАЙНА
        if kdone_zvuk in file:
            file_name = path.splitext(path.basename(file))[0]
            if file.endswith((".wav", ".mp3", ".ogg")):
                globals()[file_name] = file

    def kdone_define_assets(kdone_source, kdone_sprites_folder):
        for file in renpy.list_files():
            if kdone_source in file:
                file_name = path.splitext(path.basename(file))[0]
                if file.endswith((".png", ".jpg")):
                    if kdone_sprites_folder and '%s/%s' % (kdone_mod_folder, kdone_sprites_folder) in file:
                        renpy.image(
                            file_name,
                            ConditionSwitch(
                                "persistent.sprite_time == 'sunset'",
                                im.MatrixColor(
                                    file,
                                    im.matrix.tint(0.94, 0.82, 1.0)
                                ),
                                "persistent.sprite_time == 'night'",
                                im.MatrixColor(
                                    file,
                                    im.matrix.tint(0.63, 0.78, 0.82)
                                ),
                                "kdone_uncolorize=='lite'",
                                im.MatrixColor(
                                    file,
                                    im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722))
                                ),
                                "kdone_uncolorize=='full'",
                                im.MatrixColor(
                                    file,
                                    im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722))
                                ),
                                "True", file
                            )
                        )

                    else:
                        renpy.image(
                            file_name,
                            ConditionSwitch(
                                "kdone_uncolorize=='lite'",
                                im.MatrixColor(
                                    im.Composite((1920,1080), (0,0), file),
                                    im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722))
                                ),
                                "kdone_uncolorize=='full'",
                                im.MatrixColor(
                                    im.Composite((1920,1080), (0,0), file),
                                    im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722))
                                ),
                                True,
                                    im.Composite((1920,1080), (0,0), file)
                                )
                            )


init -15 python in kdone:

    def m(transform):
        renpy.show_layer_at(transform, layer='master')

    def s(transform):
        renpy.show_layer_at(transform, layer='screens')

    def p(time):
        renpy.pause(delay=time, hard=True)

    def pn():
        renpy.pause(hard=True)

    def b():
        renpy.block_rollback()

init python:
    def kdone_ss(vol):
        _preferences.volumes['sfx'] = vol
    
    def kdone_mm(vol):
        _preferences.volumes['music'] = vol
    
    def kdone_aa(vol):
        _preferences.volumes['voice'] = vol
    
    def kdone_hlclear():
        _history_list = []

    def kdone_newitem_uved(item):
        renpy.notify(f"Получен новый предмет! {item.name} в количестве {item.count} штук")


init python:
# РЕГЕСТРИРУЕМ ДОП КАНАЛЫ
# ЛИШНИМ НЕ БУДЕТ
# ЮЗАТЬ ТАК = play sound4 peerdune
# З.Ы. - НЕНУЖНЫЕ МОЖЕШЬ ПРОСТО УБРАТЬ
    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound_loop", "sfx", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    renpy.music.register_channel("ambience2", "voice", False)
    renpy.music.register_channel("music2", "music", False)

init python:
    
    def stop_music(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП МУЗОН (ДАБЫ ОНИ ТОЖЕ СТОПАЛИСЬ НАХ)
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "music2"):
            renpy.music.stop(channel=chnl)

    def stop_sound(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП ЗВУКИ (АНАЛОГИЧНО ВЫШЕ)
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "ambience2"):
            renpy.sound.stop(channel=chnl)

    def get_pos(channel='music'): # ДОБАВЛЯЕМ ВЫЧЕТ ПОЗИЦИИ (ИСПОЛЬЗУЕТСЯ В ДОКИ МОДАХ ДЛЯ СИНХРОНА ХУЙНИ)
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

init:
    define flash = Fade(.25, 0, .75, color="#fff")
    define flash_red = Fade(1, 0, 1, color="#e11")
    define dspr = Dissolve(.2)
    define dissolve2 = Dissolve(2.0)
    define dissolve3 = Dissolve(3.0)
    define dissolve4 = Dissolve(4)

    default persistent.rpc_mode = True

    $ kdone_define_assets('source/', kdone_sprites_folder='source/images/sprites')