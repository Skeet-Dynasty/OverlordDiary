init -1 python hide:
    
    # Сборочные настройки
    build.name = "OverlordDiary"
    config.name = "Overlord Diary"
    config.version = "1.0"
    config.window_icon = "source/gui/window_icon.png"

    # Аудио
    config.has_sound = True
    config.has_music = True
    config.has_voice = True
    # config.main_menu_music = "main-menu-theme.ogg"

    # Пользовательский интерфейс
    gui.show_name = True
    gui.about = _p("""
    """)

    # Стандартные переходы
    config.enter_transition = dissolve
    config.exit_transition = dissolve
    config.intra_transition = dissolve
    config.after_load_transition = None
    config.end_game_transition = None

    # Диалоговые окна и их переходы
    config.window = "auto"
    config.window_show_transition = Dissolve(.2)
    config.window_hide_transition = Dissolve(.2)

    # Настройки текста и авточтения
    preferences.text_cps = 75
    preferences.afm_time = 15

    # Директория сохранения
    config.save_directory = None


init python:
    
    build.directory_name = "OverlordDiary_v1.0"
    build.executable_name = "Overlord Diary"

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.md', None)
    build.classify('**.rpyb', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rar', None)
    build.classify('**.zip', None)
    build.classify('**.7z', None)

    build.archive("engine", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("video", "all")
    build.archive("font", "all")

    build.classify("game/**.jpg", "images")
    build.classify("game/**.jpeg", "images")
    build.classify("game/**.webp", "images")
    build.classify("game/**.png", "images")

    build.classify("game/**.rpyc", "engine")
    build.classify("game/**.rpy", "engine")

    build.classify("game/**.pyc", "engine")
    build.classify("game/**.py", "engine")

    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")

    build.classify("game/**.otf", "font")
    build.classify("game/**.ttf", "font")

    build.classify("game/**.webm", "video")
    build.classify("game/**.ogv", "video")
    build.classify("game/**.ogm", "video")

    build.documentation('*.html')
    build.documentation('*.txt')