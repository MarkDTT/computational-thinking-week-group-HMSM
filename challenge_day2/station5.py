def solution_station_5(name: str):
    teams = {
        1: ["Daeho", "David G", "Kaisa", "Oliver", "Sara", "Dan", "Ivar", "Lotte", "Riya", "Vassil",
            "Twan", "Ester", "Karolina", "Lena", "Margarita", "Anna", "Kien", "Klaudia", "Maliah", "Todd"],

        2: ["Oumaima", "Mathilde", "Marie-Caroline", "Anita", "Ziyan", "Bernardo", "Eleanor", "Lorijn",
            "Maria Paz", "Younes", "Yvan", "Henning", "Liangyu", "Maciej", "Toprak", "Chris",
            "GengXin", "Mingze", "Phoebe", "Madeleine"],

        3: ["Betija", "Haider", "Kacper", "Sophie P", "Amir", "Baltasar", "Isar", "Jelle", "Nicolas",
            "David C", "Ipek", "Juan", "Marfa", "Maria", "Alissa", "Leopoldo", "Mies", "Jiaying",
            "Kaixin", "Mai", "Sem", "Tibbe"],

        4: ["Justus", "Julia", "Philip", "Uli", "Vanessa", "Anna D", "Ekaterina", "Thessa", "Tongfei",
            "Yang Yang", "Benedikt", "Jan", "Nadee", "Osjah", "Tim", "Eliana", "Joana", "Peilin",
            "Pija", "Wenhao"],

        5: ["Afua", "Cristina", "Greta", "Jace", "Laura", "Anna V", "Bassant", "Ivan", "Juriaan", "Kiavash"],

        6: ["Keitaro", "Nohemi", "Norina", "Yifan", "Yinan", "Luo", "Nikola", "Olesya", "Sophie M", "Tom"]
    }

    for team, names in teams.items():
        if name in names:
            return team

    return -1


