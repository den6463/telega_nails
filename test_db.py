import sqlite3

conect = sqlite3.connect("test.db")
cursor = conect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS test(
   que_id integer PRIMARY KEY,
   que_one text,
   que_two text
   )
""")
conect.commit()


que_list = [(1,"Нюдовые тона","Френч или несложный дизайн", ),
            (2,"Гель-лак","Прозрачный лечебный"),
            (3,'В салоне','Самостоятельно'),
            (4,'Кошачьи стрелки', "Дымчатые смоки"),
            (5,"Замкнутая", "Веселая"),
            (6, "Маникюр леопардовый", "Маникюр с ромашками"),
            (7,"Однотонный","Разноцветниый"),
            (8,"Объемные худи и велосипедки","Комфортный – рубашки и штаны"),
            (9,"Яркая заколка","Крупные серьги"),
            (10,"Алекса Чанг.","Натали Портман"),
            (11,"Бархатный маникюр.","Разноцветный нейл-арт."),
            (12,"Шумное застолье в гостях у близких друзей.","Дневная вечеринка у бассейна в Лос-Анджелесе.г"),
            (13,"Теплый и уютный кашемировый шарф.","Смешная шапка с помпоном."),
            (14,"Спортивный минимализм.","Омбре с глиттером."),
            (15,"Темная помада","Яркая помада")]
cursor.executemany("INSERT INTO test VALUES(?,?,?);", que_list)

conect.commit()

