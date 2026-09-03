def solution_station_5(name):
    teams = {
        1: ["Ainas", "Ben", "Christopher", "Ebony", "Iuliia", "Klementyna", "Tiara", "Tobit", "Yasmin", "Yurui", "Yuvraj", "Zoë", "Lula", "Markus", "Mateo", "Mufang", "Muni", "Nandini", "Nathan", "Oumaima"],

        2: ["Alex", "Arwen", "Christina", "David", "Helen", "Huy Bao", "Iris", "Katharina", "Lora", "Mark", "Mats", "Minseo", "Quinn", "Rajko", "Sade", "Sylwia", "Tarling", "Vadim", "Zeno"],

        3: ["Elizabeth", "Gabriel", "Jakub", "Luc", "Soelie",
            "Aleksandra", "Arnav", "Donna", "Milan", "Rongze",
            "Cris", "Jingqi", "Oliver", "Vaayu", "Yusef",
            "Afua", "Anna", "Daniel", "Nataly", "Rafael"],

        4: ["An", "Yujie", "Douwe", "Jeremy", "Krishiv", "Lara", "Heer", "Illya", "Lucas", "Maria", "Michelle", "Neel", "Oliwia", "Paige", "Rakin", "Rapolas", "Samir", "Tom", "Yutong", "Amalia"]

    }
    name_to_lt = {n: lt for lt, names in teams.items() for n in names}

    return name_to_lt.get(name, 1)
