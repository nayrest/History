####################################################################
# QUEST v.1.0 by Eddie Braga (C) 2021
####################################################################

Paper = False
Hammer = False
Key = False
Shovel = False
Rock = False
MagicSeal = False

HayIsDigged = False
UnearthedCrypt = False
SmithyIsOpen = False
HammerIsTaked = False
GolemIsKilled = False
WizardHomeIsOpened = False
ChurchIsOpened = False
WizardIsRescued = False
WizardNotRescued = False
MagicSealTaked = False
RockIsTaked = False

CurrentLocation = 0

PlayerAnswer = 1

Disappearance = "Вы подходите к двери и пробуете открыть ее. Магический барьер с силой отбрасывает вас в сторону. Ваше тело окутывает синий туман и вы исчезаете."
Perish = "Вы медленно продвигаетесь вдоль стены у края площади. Ступени церкви уже совсем близко. Вы решаете тихо подойти ко входу церкви сбоку, но подворачиваете ногу и падаете. Голем поворачивается в вашу сторону и бросает в вас огромный камень. Вы погибаете."
NotItem = "У вас нет этого предмета для прохода."
ItemInventory = "У вас есть"
ItemAdd = "Вы взяли"
LocateUnlock = "Вы открыли"
ReadPaper = "Прежде чем пройти на эту локацию, прочитайте бумажку."
WizardHelp = 'Вы делаете шаг к дракону. Он резко взмахивает крыльями и взмывает под самый потолок. Он быстро летит к вам, открывает пасть… Внезапно прямо перед вами появляется старик с книгой и произносит какие-то непонятные слова. Дракона подхватывает неизвестная сила и начинает бросать из стороны в сторону. Внезапно он вспыхивает ярким пламенем и исчезает. Синий туман медленно растворяется. Старик поворачивается к вам и произносит - “Я же говорил, что тебе здесь не место. Все же спасибо, что освободил меня. Все, что здесь произошло - моя ошибка. Немного перепутал заклинания. А теперь уходи.”'
Congratulations = "Поздравляем, вы успешно завершили историю!"
DragonPerish = "Вы делаете шаг к дракону. Он резко взмахивает крыльями и взмывает под самый потолок. Он быстро летит к вам, открывает пасть и сжигает вас огнем. Вы погибаете."
WrongSpell = "Вы громко читаете заклинание из книги. Дракон резко взмахивает крыльями и взмывает под самый потолок. Он быстро летит к вам, открывает пасть и сжигает вас огнем. Вы погибаете."
CorrectSpell = "Вы громко читаете заклинание из книги. Дракон резко взмахивает крыльями и взмывает под самый потолок. Он быстро летит к вам, но вдруг его подхватывает неизвестная сила и начинает бросать из стороны в сторону. Внезапно он вспыхивает ярким пламенем и исчезает. Синий туман медленно растворяется."
EnteredSymbol = "Это не число. Это символ или буква."
IncorrectEnteredNumber = "Вы ввели неправильное число для продолжения сюжетной линии. Повторите попытку."
ThankYou = "Спасибо за использование приложения."
Lines = "---------------------------"
Exit = "0-выход из приложения."

PlayerInventory = []

LocationNames = ["Мост","Окраина деревни","Деревня","Вход в дом кузнеца","Дом кузнеца","Площадь перед церковью","Таверна - зал","Стол у окна в таверне","Подсобка таверны","Бумажка на столе","Стол в подсобке","Вход в дом волшебника","Дом волшебника",
    "Висящий в воздухе старик","Дом волшебника","Дом волшебника","Кладбище рядом с деревней","Склеп на кладбище","Склеп","Поле","Стог сена",
    "Каменный голем", "Стог сена", "Склеп", "Дом кузнеца", "Груда камней","Вход в дом кузнеца","Вход в дом кузнеца","Вход в дом кузнеца",
    "Вход в церковь","Церковь","Дракон"]

LocationDesc = [
    "Вечер. Вы находитесь перед обрывом, через который перекинут мост из дерева и веревок. Выглядит непрочным. Позади вас непроходимый лес. Слева от вас большое поле.",
    "Перед вами довольно большая деревня. Всю деревню накрывает какой-то зловещий туман синего цвета. Кое-где виднеются верхушки красных крыш домов. Посреди деревни в тумане виднеется здание, похожее на церковь. Справа от деревни на холме можно заметить вход на кладбище.",
    "Вы на главной улице. Вокруг никого. Тишина. Из-за тумана дальше по улице ничего не видно. Справа от вас большой дом с вывеской. На ней похоже написано Кузнец. Слева от вас дом с надписью Таверна У Грома.",
    "Вы подошли ко входу в дом кузнеца. Перед вами большая дверь с висячим замком. Похоже, что все закрыто.",
    "Здесь темно. Вокруг вас шкафы и полки, а на стенах поблескивают какие-то металлические предметы. Похоже что-то это лавка кузнеца. Справа в темном углу лежит увесистый молот. Довольно тяжелый. Им можно разбить любую деревянную дверь.",
    "Вы вышли к небольшой площади перед церковью, на которой стоит большая каменная фигура. Похоже это каменный голем. Он охраняет вход в церковь?",
    "Вы стоите посреди большого зала. Вокруг вас поломанные деревянные столы и стулья. На полу тарелки, кружки, ножи, еда. Все разбросано в беспорядке. Один стол у окна похоже уцелел. В дальнем углу зала есть дверь.",
    "Вы подходите к грубому деревянному столу. Среди кружек и тарелок вы видите маленькую бумажку на которой что-то написано мелким почерком.",
    "Вы в плохо освещенном помещении, вокруг вас множество бочек и ящиков, с потолка свисают копченые колбасы. Свозь маленькое окошко на противоположной стене слабо светит закатное солнце. У окна на столе что-то блестит.",
    '"Местный волшебник Эвато Корвариус. Защитные амулеты и зелья. Адрес: второй дом направо за кузницей."',
    'На столе среди холщовых мешков и нарезанной бечевки для колбас лежит потертый ключ. На нем можно разглядеть выдавленную небольшую букву "К".',
    "Вы перед домом волшебника. С входной дверью творится что-то странное. Она закрыта каким-то магическим барьером.",
    "Посередине большой комнаты в воздухе висит старик в странной одежде, покрытой какими-то знаками. Старика окружает какое-то синее облако. Вокруг вас стоят столы с банками и сосудами, непонятными предметами. Полки на стенах завалены книгами. Похоже старик попал в какую-то магическую ловушку и не может освободиться. Глаза его закрыты. Он спит?",
    'Вы медленно приближаетесь. Вдруг старик резко открывает глаза. "Ты еще кто такой? Как попал сюда, а? А ну быстро подай мне вон ту синюю книгу со звездой и проваливай отсюда!" - злобно прошипел старикашка и кивнул в сторону большого стола, где посреди разного хлама лежала увесистая книга.',
    'Старик ехидно улыбнулся. "Что произошло? Это не твое дело! Я же сказал - подай книгу и убирайся! Странно, что ты еще жив." После этих слов он попытался дотянуться до стола.',
    'Вы протягиваете старику книгу. Он резко вырывает ее у вас из рук и начинает судорожно ее листать. Найдя нужную страницу он минуту что-то бормочет себе под нос. Вдруг облако исчезает и он падает на землю. Встает и отряхиваясь говорит - "Чего уставился? У меня нет настроения вести пустые разговоры. Уходи отсюда пока ты еще жив." После этих слов он вместе с книгой растворяется в воздухе.',
    "Вы на старом деревенском кладбище. Вас окружают старые покосившиеся надгробия, всюду зловещий синий туман. Посреди кладбища виднеется большой склеп. Он наполовину ушел под землю.",
    "Похоже склеп очень старый. Он наклонился влево, вход почти полностью ушел под землю.",
    'Вы внутри склепа. Темно. Свет узким лучом сквозь прокопанный вход освещает могильную плиту с четырьмя львами вокруг звезды странной формы. Можно различить полустертые буквы "Corv...". В углу лежит круглый камень с изображением льва.',
    "Вы на поле. Похоже что часть травы уже скосили и собрали в большие стога.",
    "Обычный стог сена. Большой. Похоже, что вся трава уже высохла.",
    "Вы тихо подкрадываетесь к голему сзади и со всех сил бросаете камень. Камень со свистом летит и попадает прямо в голову голема. Он рассыпается на мелкие камни. Вы подходите к груде камней и видите какой-то светящийся предмет.",
    "Раскопанный вами стог сена. Больше здесь ничего нет.",
    "Откопанный вами склеп. Больше здесь ничего нет.",
    "Здесь темно. Вокруг вас шкафы и полки, а на стенах поблескивают какие-то металлические предметы. Похоже что-то это лавка кузнеца.",
    "Перед вами груда камней. Это все что осталось от голема.",
    "Вы подошли ко входу в дом кузнеца. Входная дверь открыта.",
    "Вы подошли ко входу в дом кузнеца. Входная дверь открыта.",
    "Вы подошли ко входу в дом кузнеца. Перед вами большая дверь с висячим замком. Похоже, что все закрыто.",
    "Перед вами массивные двустворчатые дубовые двери. Похоже что они заперты. Изнутри церкви доносятся странные звуки.",
    "Вы находитесь в большом зале с колоннами и высоким потолком. В конце зала у алтаря стоит на задних лапах огромный красный дракон. Вокруг вас стены и пол покрывает плотный синий туман.",
    "Вы медленно подходите к дракону. Похоже что он вас пока не заметил. Вы открываете книгу там, где заложена закладка. Перед вами три заклинания. Наверное одно из них может уничтожить дракона..."]

PlayerNavigationOptions = [
    "1-пройти через мост.\n2-выйти на поле.\n3-пройти мимо.",
    "1-войти в деревню.\n2-вернуться к мосту.\n3-обойти деревню и подойти к кладбищу.",
    "1-подойти к кузнице\n2-подойти к таверне\n3-пройти дальше по улице\n4-вернуться к мосту",
    "1-вернуться на главную улицу\n2-попробовать открыть дверь ключом и войти.\n3-пройти к дому волшебника.",
    "1-Взять молот\n2-Выйти из дома.",
    "1-прокрасться мимо голема к церкви, возможно он не заметит.\n2-вернуться на главную улицу\n3-подкрасться поближе к голему и бросить в него камень.",
    "1-Подойти к столу у окна\n2-Зайти в дверь.\n3-Выйти из таверны.",
    "1-Прочитать бумажку.\n2-Вернуться в зал.",
    "1-подойти к столу\n2-вернуться в зал таверны",
    "1-назад",
    "1-взять ключ\n2-вернуться к двери",
    "1-попробовать открыть дверь силой.\n2-вернуться к кузнице.\n3-приложить к двери магическую печать",
    "1-подойти к старику.\n2-выйти из дома",
    "1-спросить что произошло\n2-подать ему книгу\n3-забрать синюю книгу себе и выйти из дома",
    "1-подать ему книгу\n2-забрать синюю книгу себе и выйти из дома\n3-выйти из дома",
    "1-выйти из дома волшебника",
    "1-подойти к склепу\n2-уйти с кладбища",
    "1-вернуться на кладбище\n2-откопать вход в склеп лопатой",
    "1-взять камень\n2-выйти из склепа",
    "1-подойти к ближайшему стогу сена\n2-вернуться к мосту",
    "1-порыться в сене\n2-вернуться на поле",
    "1-подобрать предмет\n2-подойти к входу в церковь\n3-вернуться на главную улицу",
    "1-вернуться на поле",
    "1-вернуться на кладбище",
    "1-Выйти из дома",
    "1-подойти к входу в церковь\n2-вернуться на главную улицу",
    "1-вернуться на главную улицу\n2-войти в дом\n3-пройти к дому волшебника",
    "1-вернуться на главную улицу\n2-войти в дом",
    "1-вернуться на главную улицу\n2-попробовать открыть дверь ключом и войти",
    "1-разбить двери молотом и войти\n2-вернуться к останкам голема",
    "1-приблизиться к дракону - Битва с драконом.\n2-выйти из церкви",
    "1-первое заклинание\n2-второе заклинание\n3-третье заклинание"]

PlayerItemNames = ["Ключ", "Молот","Синяя книга","Камень","Лопата","Магическая печать"]
PlayerItemDescriptions = ["Обычный бронзовый ключ с буквой К", "Большой тяжелый молот. Наверное им можно выбить дверь.","Старая синяя книга. Похоже содержит магические заклинания. Тут есть закладка.",
    "Странный круглый камень с изображением льва.","Старая лопата. Черенок гнилой, но копать еще можно.","Светящийся круглый предмет с изображением звезды необычной формы. Похоже сделан из неизвестного камня."]

def AddItemToInventory(Item):
    if Item not in PlayerInventory:
        PlayerInventory.append(Item)
    elif Item in PlayerInventory:
        print(ItemInventory, Item)

def RemoveItemFromInventory(Item):
    PlayerInventory.remove(Item)

def ItemIsReceived(Item):
    AddItemToInventory(PlayerItemNames[Item])
    print(ItemAdd, PlayerItemNames[Item])
    print(Lines)
    print(PlayerItemDescriptions[Item])
    print(Lines)


while PlayerAnswer != "0":
    try:
        print(LocationNames[CurrentLocation])
        print(Lines)
        print(LocationDesc[CurrentLocation])
        print(Lines)
        print(Exit,"\n")
        print("Ваш инвентарь:", PlayerInventory,"\n")
        print(PlayerNavigationOptions[CurrentLocation])
        PlayerAnswer = int(input())
    except:
        print(EnteredSymbol)
        continue

    #Bridge
    if CurrentLocation == 0:
        #Pass to Village Entrance
        if PlayerAnswer == 1:
            CurrentLocation = 1
        elif PlayerAnswer == 2:
            CurrentLocation = 19
        elif PlayerAnswer == 3:
            print(ThankYou)
            exit()
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Village
    elif CurrentLocation == 1:
        if PlayerAnswer == 1:
            CurrentLocation = 2
        elif PlayerAnswer == 2:
            CurrentLocation = 0
        elif PlayerAnswer == 3:
            CurrentLocation = 16
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Main Street Village
    elif CurrentLocation == 2:
        if PlayerAnswer == 1 and not SmithyIsOpen and not WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 3
        elif PlayerAnswer == 1 and SmithyIsOpen and not WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 26
        elif PlayerAnswer == 1 and SmithyIsOpen and WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 1 and SmithyIsOpen and not WizardIsRescued and WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 1 and not SmithyIsOpen and not WizardIsRescued and WizardNotRescued:
            CurrentLocation = 28
        elif PlayerAnswer == 1 and not SmithyIsOpen and WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 28
        elif PlayerAnswer == 2:
            CurrentLocation = 6
        elif PlayerAnswer == 3 and not GolemIsKilled:
            CurrentLocation = 5
        elif PlayerAnswer == 3 and GolemIsKilled and not MagicSealTaked:
            CurrentLocation = 21
        elif PlayerAnswer == 3 and MagicSealTaked:
            CurrentLocation = 25
        elif PlayerAnswer == 4:
            CurrentLocation = 0
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Smithy Entrance
    elif CurrentLocation == 3:
        if PlayerAnswer == 1:
            CurrentLocation = 2
        elif PlayerAnswer == 2 and not SmithyIsOpen and Key:
            RemoveItemFromInventory("Ключ")
            Key = False
            SmithyIsOpen = True
            CurrentLocation = 4
            print(LocateUnlock, LocationNames[CurrentLocation])
        elif PlayerAnswer == 2 and SmithyIsOpen:
            CurrentLocation = 4
        elif PlayerAnswer == 2 and not Key:
            print(NotItem)
        elif PlayerAnswer == 3 and Paper:
            CurrentLocation = 11
        elif PlayerAnswer == 3 and not Paper:
            print(ReadPaper)
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 26:
        if PlayerAnswer == 1:
            CurrentLocation = 2
        elif PlayerAnswer == 2 and not SmithyIsOpen and Key:
            RemoveItemFromInventory("Ключ")
            Key = False
            SmithyIsOpen = True
            CurrentLocation = 4
            print(LocateUnlock, LocationNames[CurrentLocation])
        elif PlayerAnswer == 2 and SmithyIsOpen:
            CurrentLocation = 4
        elif PlayerAnswer == 2 and not Key:
            print(NotItem)
        elif PlayerAnswer == 3 and Paper:
            CurrentLocation = 11
        elif PlayerAnswer == 3 and not Paper:
            print(ReadPaper)
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 27:
        if PlayerAnswer == 1:
            CurrentLocation = 2
        elif PlayerAnswer == 2 and not SmithyIsOpen and Key:
            RemoveItemFromInventory("Ключ")
            Key = False
            SmithyIsOpen = True
            CurrentLocation = 4
            print(LocateUnlock, LocationNames[CurrentLocation])
        elif PlayerAnswer == 2 and SmithyIsOpen and not HammerIsTaked:
            CurrentLocation = 4
        elif PlayerAnswer == 2 and SmithyIsOpen and HammerIsTaked:
            CurrentLocation = 24
        elif PlayerAnswer == 2 and not Key:
            print(NotItem)
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 28:
        if PlayerAnswer == 1:
            CurrentLocation = 2
        elif PlayerAnswer == 2 and not SmithyIsOpen and Key:
            RemoveItemFromInventory("Ключ")
            Key = False
            SmithyIsOpen = True
            CurrentLocation = 4
            print(LocateUnlock, LocationNames[CurrentLocation])
        elif PlayerAnswer == 2 and SmithyIsOpen:
            CurrentLocation = 4
        elif PlayerAnswer == 2 and not Key:
            print(NotItem)
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Smithy
    elif CurrentLocation == 4:
        if PlayerAnswer == 1:
            Hammer = True
            HammerIsTaked = True
            ItemIsReceived(1)
        elif PlayerAnswer == 2 and not Hammer and not WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 26
        elif PlayerAnswer == 2 and not Hammer and WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 2 and not Hammer and not WizardIsRescued and WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 2 and Hammer and not WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 26
        elif PlayerAnswer == 2 and Hammer and not WizardIsRescued and WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 2 and Hammer and WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Square
    elif CurrentLocation == 5:
        if PlayerAnswer == 1:
            print(Perish)
            exit()
        elif PlayerAnswer == 2:
            CurrentLocation = 2
        elif PlayerAnswer == 3 and Rock:
            RemoveItemFromInventory("Камень")
            Rock = False
            GolemIsKilled = True
            CurrentLocation = 21
        elif PlayerAnswer == 3 and not Rock:
            print(NotItem)
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Inn
    elif CurrentLocation == 6:
        if PlayerAnswer == 1:
            CurrentLocation = 7
        elif PlayerAnswer == 2:
            CurrentLocation = 8
        elif PlayerAnswer == 3:
            CurrentLocation = 2
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Table In The Inn
    elif CurrentLocation == 7:
        if PlayerAnswer == 1:
            Paper = True
            CurrentLocation = 9
        elif PlayerAnswer == 2:
            CurrentLocation = 6
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Paper On The Table
    elif CurrentLocation == 9:
        if PlayerAnswer == 1:
            CurrentLocation = 7
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Inn Utility
    elif CurrentLocation == 8:
        if PlayerAnswer == 1:
            CurrentLocation = 10
        elif PlayerAnswer == 2:
            CurrentLocation = 6
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #InnUtilityTable
    elif CurrentLocation == 10:
        if PlayerAnswer == 1:
            Key = True
            ItemIsReceived(0)
        elif PlayerAnswer == 2:
            CurrentLocation = 8
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #The entrance to the wizard's house
    elif CurrentLocation == 11:
        if PlayerAnswer == 1:
            print(Disappearance)
            exit()
        elif PlayerAnswer == 2:
            CurrentLocation = 3
        elif PlayerAnswer == 3 and not WizardHomeIsOpened and MagicSeal:
            RemoveItemFromInventory("Магическая печать")
            MagicSeal = False
            WizardHomeIsOpened = True
            CurrentLocation = 12
        elif PlayerAnswer == 3 and WizardHomeIsOpened:
            CurrentLocation = 12
        elif PlayerAnswer == 3 and not MagicSeal:
            print(NotItem)
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Wizard's house
    elif CurrentLocation == 12:
        if PlayerAnswer == 1:
            CurrentLocation = 13
        elif PlayerAnswer == 2:
            CurrentLocation = 11
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Old man
    elif CurrentLocation == 13:
        if PlayerAnswer == 1:
            CurrentLocation = 14
        elif PlayerAnswer == 2:
            WizardIsRescued = True
            CurrentLocation = 15
        elif PlayerAnswer == 3 and SmithyIsOpen:
            ItemIsReceived(2)
            WizardNotRescued = True
            CurrentLocation = 27
        elif PlayerAnswer == 3 and not SmithyIsOpen:
            ItemIsReceived(2)
            WizardNotRescued = True
            CurrentLocation = 28
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 14:
        if PlayerAnswer == 1:
            WizardIsRescued = True
            CurrentLocation = 15
        elif PlayerAnswer == 2 and SmithyIsOpen:
            ItemIsReceived(2)
            WizardNotRescued = True
            CurrentLocation = 27
        elif PlayerAnswer == 2 and not SmithyIsOpen:
            ItemIsReceived(2)
            WizardNotRescued = True
            CurrentLocation = 28
        elif PlayerAnswer == 3:
            CurrentLocation = 3
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 15:
        if PlayerAnswer == 1 and SmithyIsOpen:
            CurrentLocation = 27
        elif PlayerAnswer == 1 and not SmithyIsOpen:
            CurrentLocation = 28
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Cemetery
    elif CurrentLocation == 16:
        if PlayerAnswer == 1 and not UnearthedCrypt:
            CurrentLocation = 17
        elif PlayerAnswer == 1 and UnearthedCrypt:
            CurrentLocation = 23
        elif PlayerAnswer == 2:
            CurrentLocation = 1
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Crypt Entrance
    elif CurrentLocation == 17:
        if PlayerAnswer == 1:
            CurrentLocation = 16
        elif PlayerAnswer == 2 and not UnearthedCrypt and Shovel:
            RemoveItemFromInventory("Лопата")
            Shovel = False
            UnearthedCrypt = True
            CurrentLocation = 18
        elif PlayerAnswer == 2 and UnearthedCrypt and not RockIsTaked:
            CurrentLocation = 18
        elif PlayerAnswer == 2 and UnearthedCrypt and RockIsTaked:
            CurrentLocation = 23
        elif PlayerAnswer == 2 and not Shovel:
            print(NotItem)
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Crypt
    elif CurrentLocation == 18:
        if PlayerAnswer == 1:
            ItemIsReceived(3)
            Rock = True
            RockIsTaked = True
        elif PlayerAnswer == 2 and not RockIsTaked:
            CurrentLocation = 17
        elif PlayerAnswer == 2 and RockIsTaked:
            CurrentLocation = 23
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Field
    elif CurrentLocation == 19:
        if PlayerAnswer == 1 and not HayIsDigged:
            CurrentLocation = 20
        elif PlayerAnswer == 1 and HayIsDigged:
            CurrentLocation = 22
        elif PlayerAnswer == 2:
            CurrentLocation = 0
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #A stack of hay
    elif CurrentLocation == 20:
        if PlayerAnswer == 1:
            ItemIsReceived(4)
            HayIsDigged = True
            Shovel = True
        elif PlayerAnswer == 2:
            CurrentLocation = 19
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 22:
        if PlayerAnswer == 1:
            CurrentLocation = 19
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Killed Golem
    elif CurrentLocation == 21:
        if PlayerAnswer == 1:
            ItemIsReceived(5)
            MagicSeal = True
            MagicSealTaked = True
        elif PlayerAnswer == 2:
            CurrentLocation = 29
        elif PlayerAnswer == 3:
            CurrentLocation = 2
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 25:
        if PlayerAnswer == 1:
            CurrentLocation = 29
        elif PlayerAnswer == 2:
            CurrentLocation = 2
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 23:
        if PlayerAnswer == 1:
            CurrentLocation = 16
        else:
            print(IncorrectEnteredNumber)
    elif CurrentLocation == 24:
        if PlayerAnswer == 1 and not WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 26
        elif PlayerAnswer == 1 and WizardIsRescued and not WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 1 and not WizardIsRescued and WizardNotRescued:
            CurrentLocation = 27
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Church entrance
    elif CurrentLocation == 29:
        if PlayerAnswer == 1 and not ChurchIsOpened:
            RemoveItemFromInventory("Молот")
            Hammer = False
            ChurchIsOpened = True
            CurrentLocation = 30
        elif PlayerAnswer == 1 and ChurchIsOpened:
            CurrentLocation = 30
        elif PlayerAnswer == 2:
            CurrentLocation = 25
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    #Church
    elif CurrentLocation == 30:
        if PlayerAnswer == 1 and not WizardIsRescued and WizardNotRescued:
            CurrentLocation = 31
        elif PlayerAnswer == 1 and WizardIsRescued and not WizardNotRescued:
            print(WizardHelp)
            print(Congratulations)
            exit()
        elif PlayerAnswer == 1 and not WizardIsRescued and not WizardNotRescued:
            print(DragonPerish)
            exit()
        elif PlayerAnswer == 2:
            CurrentLocation = 29
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)

    elif CurrentLocation == 31:
        if PlayerAnswer == 1:
            print(WrongSpell)
            exit()
        elif PlayerAnswer == 2:
            print(WrongSpell)
            exit()
        elif PlayerAnswer == 3:
            print(CorrectSpell)
            print(Congratulations)
            exit()
        elif PlayerAnswer == 0:
            print(ThankYou)
            exit()
        else:
            print(IncorrectEnteredNumber)
    
