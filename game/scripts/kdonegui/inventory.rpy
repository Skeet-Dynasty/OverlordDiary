# СИСТЕМА ИНВЕНТАРЯ
# MADE BY @b3rg3n
# Since 2025 (c)
# Skeet Dynasty

init python:
    class inventoryItem:
        def __init__(self, name, description, type, storage, count, icon, status, action):
            self.name = name
            self.description = description
            self.type = type # ЛИБО MOBILE, ЛИБО GUN, ЛИБО NOTE
            self.storage = storage # ЛИБО BAG, ЛИБО POCKETS
            self.count = count
            self.icon = icon
            self.status = status # БУЛЕВАЯ ПЕРЕМЕННАЯ ДОСТУПНОСТИ ИГРОКУ
            self.action = action # НАЗВАНИЕ ФУНКЦИИ ДЕЙСТВИЯ

        def check(self):
            print(f"Название: {self.name}\nОписание: {self.description}\nТип: {self.type}\nГде лежит: {self.storage}\nКоличество: {self.count}\nИконка: {self.icon}\nДоступность: {self.status}\nДействие: {self.action}")

        def changestatus(self, newstatus):
            self.status = newstatus

        def changecount(self, newcount):
            self.count = newcount

    ifone = inventoryItem("Iphone 6s", "На своё время неплохая мобила, однако сейчас с неё можно лишь набрать бывшую (если бы у Данилы она была), да поплакаться, как жизнь хуёва.", "Mobile", "Bag", 1, "source/images/icons/ifone.png", True, "take_alo")