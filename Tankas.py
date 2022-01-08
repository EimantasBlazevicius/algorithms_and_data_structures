import random
"""
Klasė: Tankas
Metodai: pirmyn, atgal, kairėn, dešinėn, šūvis, info, ...

Kintamieji turi:
saugoti tanko koordinates,
saugoti tanko kryptį,
saugoti šūvių skaičių į kiekvieną kryptį.

Tankas gali judėti pirmyn (į Šiaurę), 
dešinėn (į Rytus), 
atgal (į Pietus), 
kairėn (į Vakarus) per vieną poziciją. 
Pvz. „tankas pajuda kairėn", 
tai reiškia jis pasisuko 90 laipsnių ir pajudėjo per vieną vienetą į Vakarus.

Tankas gali šaudyti tik ta kryptimi, į kurią jis yra pasisukęs.
Metodas info() turi parodyti:

į kurią kryptį tankas šiuo metu yra pasisukęs,
kokios yra jo koordinatės,
kiek iš viso atliko šūvių
kiek atliko šūvių į kiekvieną kryptį atskirai.
Visas tanko ir informacijos valdymas turi būti atliktas konsolėje (grafinio interfeiso nereikia). 
Tam reikės sukurti meniu ir priimti vartotojo nurodymai. Veiksmai turi būti atliekami (kviečiami metodai) tol, 
kol vartotojas nesustabdys programos (pavyzdžiui, pasirinkęs tam tikrą meniu punktą).

2 etapas
Patobulinkite programą taip, kad koordinačių sistemoje būtų generuojamas taikinys. 
Tanko užduotis - atsidurti tinkamoje pozicijoje ir reikiama kryptimi, kad iššovus būtų fiksuojamas pataikymas. 
Tankui pataikius, konsolėje matome užrašą "pataikei" ir tuoj pat sugeneruojamas naujas taikinys.

3 etapas
Sugalvokite taškų sistemą, pvz už pataikymus galima skirti 100 taškų, 
už kiekvieną kitą veiksmą nubraukti 10 taškų. Sumuoti pataikymus. 
Pasibaigus taškams programa parodo, kiek numušta taikinių, ir pasibaigia. 
Galbūt galima saugoti high scores - pasibaigus įvedamas vardas ir žaidėjas su numuštų 
taikinių skaičiumi įrašomas į topus. Topus galbūt galima pažiūrėti su komanda 'top'. 
Sugalvokite kokių nors savo patobulinimų, sėkmės :)
"""


class Tank:
    """
    Tanko klasė su visais tanko metodais
    """
    def __init__(self):
        """
        Inicijuojam koordinates x ir y kad tankas stovi 0:0 pozicijoje
         ir yra atsisukęs į y teigiamą pusę arba į viršų.
         Inicijuoti šūvių kiekių ir šūvių kiekviena kryptimi kintamieji.
        """
        self.x = 0
        self.y = 0
        self.direction = 'up'
        self.shot_directions = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
        self.targets_hit = 0

    def move(self, direction_to_move):
        """
           Funkcija atakinga už tanko judėjimą
        """
        self.direction = direction_to_move
        if direction_to_move == 'up':
            self.y += 1  # Tankas pavažiavo į priekį
        elif direction_to_move == 'down':
            self.y -= 1  # Tankas pavažiavo į atgal
        elif direction_to_move == 'left':
            self.x -= 1  # Tankas pavažiavo į kairę
        elif direction_to_move == 'right':
            self.x += 1  # Tankas pavažiavo į dešinę

    def shoot(self, targetx, targety):
        """
        Tikrinimas vyksta pagal logiką kad jeigu tankas stovi pizicijoje
        kuri yra lygi taikinio x, arba taikinio y reikšmei,
        ir tanko kryptis atitinka logiką kad jis žiūri yra y arba x reikšmę
        atitinkamai, šūvis bus sėkmingas.

        :param targetx: Taikinio pozicijos x reikšmė
        :param targety: Taikinio pozicijos y reikšmė
        :return: True jeigu pataikom į taikinį, kitu atveju, gražinam False
        """
        print('Shot done!')
        self.shot_directions[self.direction] += 1
        if self.x == targetx:
            if self.y < targety:
                if self.direction == 'up':
                    self.targets_hit += 1
                    return True
            else:
                if self.direction == 'down':
                    self.targets_hit += 1
                    return True
        if self.y == targety:
            if self.x < targetx:
                if self.direction == 'right':
                    self.targets_hit += 1
                    return True
            else:
                if self.direction == 'left':
                    self.targets_hit += 1
                    return True

        return False

    def info(self):
        """
        Funkcija atsakinga už klasės informacijos atspausdinimą ekrane.
        :return: nieko
        """
        print(f"Kryptis: {self.direction}")
        print(f"Koordinatės: {self.x}:{self.y}")
        print(f"Šūvių iš viso: {sum(self.shot_directions.values())}")
        print(f"{self.shot_directions}")
        print((f"Targets Hit: {self.targets_hit}"))


class Target:
    """
    Klasė nurodyti taikinio savybėms ir funkcionalumui
    """
    def __init__(self):
        """
        Inicijuojam taikinio lokaciją kur x ir y kreikšmės bus sugeneruotos random rėžiuose nuo -5 iki 5
        """
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)

    def reset(self):
        """
         Per naują nustatom taikinio lokaciją kur x ir y kreikšmės bus sugeneruotos random rėžiuose nuo -5 iki 5.
         Turėtų būti panaudojamas kai taikinys buvo sunaikintas.
         """
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)


tankutis = Tank()
takinys = Target()
POINTS = 100

print("Sveiki, Taisyklės kaip žaisti")
while POINTS != 0:  # Programa veiks kol taškai nesibaigs.
    print("Judesiai:")
    print("w: aukštyn, s: žemyn, a: kairėn, d: dešinėn")
    print("b: Boom, i: informacija, q: išeiti")
    print(f"x: {tankutis.x}, y: {tankutis.y}")
    x = str(input("Tavo pasirinkimas: "))
    POINTS -= 10  # už kiekvieną ėjimą nuskaitomi 10 taškų

    if x == 'w':
        tankutis.move('up')
    elif x == 's':
        tankutis.move('down')
    elif x == 'a':
        tankutis.move('left')
    elif x == 'd':
        tankutis.move('right')
    elif x == 'b':
        if tankutis.shoot(takinys.x, takinys.y):
            print('Pataikei')
            POINTS += 50  # Pataikius pridedami 50 taškų
            takinys.reset()  # Per naują nustatomas taikinys
    elif x == 'i':
        tankutis.info()
    elif x == "q":
        print("GG")
        print(f"Targets Hit: {tankutis.targets_hit}")
        break
    elif x == "c":
        print(f"{takinys.x}: {takinys.y}")

print("Taškai baigėsi, ko dar nori?")
