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

    inventory_items = []

    ifone = inventoryItem("Iphone 6s", "На своё время неплохая мобила, однако сейчас с неё можно лишь набрать бывшую (если бы у Данилы она была), да поплакаться, как жизнь хуёва.", "Mobile", "Bag", 1, "source/images/icons/ifone.png", True, "take_alo")
    inventory_items.append(ifone)

    fimoz = inventoryItem("Фимозный хуй", "Писюн, размером чуть меньше среднего. Как главный недостаток - крайняя плоть прилипла к головке. Можно попробовать растянуть.", "Dick", "Pockets", 1, "source/images/icons/fimoz.png", True, "check_fimoz")
    inventory_items.append(fimoz)

    cigi = inventoryItem("Сигареты <<Максим>> Красный", "Ядрёно-ядерные сижки, от которых можно и выплюнуть свои лёгкие на асфальт. Но в психушке выбирать не из чего...", "item", "Pockets", 18, "source/images/icons/cigi.png", False, "try_smoke")
    inventory_items.append(cigi)

    kdone_bag_vernuli = False # ПЕРЕМЕННАЯ ВОЗВРАТА САНИТАРАМИ СУМКИ С МОБИЛОЙ
    kdone_invent_dostup = False # ПЕРЕМЕННАЯ ДОСТУПНОСТИ ИНВЕНТАРЯ (НЕ СРАЗУ ЖЕ ДАВАТЬ БЛЯДЬ)

    def take_alo():
        renpy.notify("Пока в разработке...")

    def try_smoke():
        renpy.notify("Пока в разработке...")

    def check_fimoz():
        renpy.notify("Пока в разработке...")

screen kdone_inventory():
    tag menu
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        
        vbox:
            spacing 20
            
            if kdone_bag_vernuli:
                label "Сумка" xalign 0.5 ypos 0.5
                vbox:
                    for item in [i for i in inventory_items if i.storage == "Bag" and i.status]:
                        button:
                            action Function(globals().get(item.action, None))
                            sensitive item.status
                            background None
                            xfill True
                            
                            hbox:
                                spacing 10
                                add item.icon
                                vbox:
                                    text "[item.name] x[item.count]"
                                    text "[item.description]" size 17

            label "Карманы" xalign 0.5 ypos 0.5
            vbox:
                for item in [i for i in inventory_items if i.storage == "Pockets" and i.status]:
                    button:
                        action Function(globals().get(item.action, None))
                        sensitive item.status
                        background None
                        xfill True
                        
                        hbox:
                            spacing 10
                            add item.icon
                            vbox:
                                text "[item.name] x[item.count]"
                                text "[item.description]" size 17

            textbutton "Вернуться к насущным делам" action Return() xalign 0.5