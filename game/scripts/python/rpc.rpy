# TRUE STORY DISCORD RPC
# by @b3rg3n
# since 2024

init python:
    from pypresence import DiscordNotFound # ИМПОРТИРУЕМ НУЖНУЮ ОШИБКУ ПИТОНА (ЛЕЖАТ В python-packages)
    from pypresence import Presence # ИМПОРТИРУЕМ НУЖНУЮ ФУНКЦИЮ ПИТОНА (ЛЕЖАТ В python-packages)
    import time # ИМПОРТИРУЕМ ВРЕМЯ ДЛЯ СЧЁТЧИКА

    rpc = Presence("1408925190423056475") # ID ХУЕТЫ

    if persistent.rpc_mode:
        try:
            rpc.connect() # ПОДКЛЮЧЕНИЕ К ДС
        except DiscordNotFound:
            pass
        except ConnectionRefusedError:
            pass
    else:
        pass

    def rpc_update(state, details, large_image, start=None):
        if persistent.rpc_mode:
            try:
                rpc.update(state=state, details=details, large_image=large_image, start=start or time.time())
            except AssertionError:
                pass

init:
    default persistent.rpc_mode = True